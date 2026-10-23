import * as XLSX from 'xlsx';
import type { DepartamentoId } from '@/types';
import { UNIT_INDICATORS_CONFIG } from './excelTemplates';

export interface ParsedBatchItem {
  indicador_codigo: string;
  indicador_nombre: string;
  unidad_medida: string;
  meta_periodo: number;
  valor_registrado: number;
  observaciones: string;
  isValid: boolean;
  error?: string;
}

export interface ExcelParseResult {
  success: boolean;
  departamento_codigo: DepartamentoId;
  totalRows: number;
  validRows: number;
  items: ParsedBatchItem[];
  errors: string[];
  warnings: string[];
}

function cleanNumericValue(val: any): number {
  if (typeof val === 'number') return val;
  if (val === null || val === undefined || val === '') return NaN;
  let s = String(val).trim().replace(/%/g, '').trim();
  
  // Si tiene formato de miles como 25.000 o 25,000 sin decimales
  if (/^\d{1,3}[.,]\d{3}$/.test(s)) {
    s = s.replace(/[.,]/g, '');
  } else if (/^\d{1,3}[.,]\d{3}[.,]\d{2,4}$/.test(s)) {
    // Ejemplo: 1.361,00 o 1,361.00
    if (s.includes(',') && s.lastIndexOf(',') > s.lastIndexOf('.')) {
      s = s.replace(/\./g, '').replace(',', '.');
    } else {
      s = s.replace(/,/g, '');
    }
  } else {
    // Caso simple decimal con coma: 99,49 -> 99.49
    s = s.replace(',', '.');
  }

  const n = parseFloat(s);
  return isNaN(n) ? NaN : n;
}

export async function parseUnitExcelFile(file: File, targetDept: DepartamentoId): Promise<ExcelParseResult> {
  const result: ExcelParseResult = {
    success: false,
    departamento_codigo: targetDept,
    totalRows: 0,
    validRows: 0,
    items: [],
    errors: [],
    warnings: [],
  };

  try {
    const arrayBuffer = await file.arrayBuffer();
    const wb = XLSX.read(arrayBuffer, { type: 'array' });

    if (!wb.SheetNames.length) {
      result.errors.push('El archivo Excel no contiene ninguna hoja de cálculo.');
      return result;
    }

    // Buscar la hoja correspondiente por nombre o usar la primera
    const sheetName = wb.SheetNames.find((name) =>
      name.toLowerCase().includes(targetDept.toLowerCase()) ||
      name.toLowerCase().includes('carga') ||
      name.toLowerCase().includes('indicador')
    ) || wb.SheetNames[0];

    const ws = wb.Sheets[sheetName];

    if (!ws) {
      result.errors.push(`No se pudo leer la hoja ${sheetName}.`);
      return result;
    }

    const rows: any[][] = XLSX.utils.sheet_to_json(ws, { header: 1, defval: '' });

    if (!rows || rows.length < 3) {
      result.errors.push('El archivo no posee suficientes filas de información.');
      return result;
    }

    // Localizar dinámicamente la fila de encabezados
    let headerRowIndex = -1;
    let colCodigo = 0;
    let colNombre = 1;
    let colUnidad = 2;
    let colMeta = 3;
    let colValor = 4;
    let colObs = 5;

    for (let i = 0; i < Math.min(15, rows.length); i++) {
      const row = rows[i];
      if (!row || !Array.isArray(row)) continue;

      const rowLower = row.map((c) => String(c).toLowerCase().trim());
      const hasCode = rowLower.some((c) => c.includes('código') || c.includes('codigo') || c === 'cod');
      const hasValue = rowLower.some((c) => c.includes('valor') || c.includes('reportado') || c.includes('cifra') || c.includes('real'));

      if (hasCode || (hasValue && rowLower.some((c) => c.includes('indicador')))) {
        headerRowIndex = i;
        // Detectar índices dinámicos de columnas
        rowLower.forEach((c, idx) => {
          if (c.includes('código') || c.includes('codigo') || c === 'cod') colCodigo = idx;
          else if (c.includes('nombre') || c.includes('indicador')) colNombre = idx;
          else if (c.includes('unidad') || c.includes('medida')) colUnidad = idx;
          else if (c.includes('meta')) colMeta = idx;
          else if (c.includes('valor') || c.includes('reportado') || c.includes('cifra') || c.includes('real')) colValor = idx;
          else if (c.includes('observaci') || c.includes('justifica')) colObs = idx;
        });
        break;
      }
    }

    if (headerRowIndex === -1) {
      // Si no encontró encabezados explícitos, asumir estructura estándar desde fila 4 (índice 4)
      headerRowIndex = 3;
    }

    const validConfigs = UNIT_INDICATORS_CONFIG[targetDept]?.indicators || [];
    const validConfigMap = new Map(validConfigs.map((i) => [i.codigo.toUpperCase(), i]));

    for (let i = headerRowIndex + 1; i < rows.length; i++) {
      const row = rows[i];
      if (!row || !row[colCodigo]) continue;

      const rawCode = String(row[colCodigo]).trim().toUpperCase();
      if (!rawCode || rawCode.length < 3) continue;

      // Buscar si coincide con alguno de los códigos oficiales
      const matchedConfig = validConfigMap.get(rawCode) || Array.from(validConfigMap.values()).find((cfg) =>
        rawCode.includes(cfg.codigo) || cfg.codigo.includes(rawCode)
      );

      const nombre = String(row[colNombre] || (matchedConfig ? matchedConfig.nombre : '')).trim();
      const unidad = String(row[colUnidad] || (matchedConfig ? matchedConfig.unidad_medida : '')).trim();
      const rawMeta = row[colMeta];
      const rawValor = row[colValor];
      const obs = String(row[colObs] || '').trim();

      const meta = cleanNumericValue(rawMeta) || (matchedConfig ? matchedConfig.meta : 0);
      const valor = cleanNumericValue(rawValor);

      let isValid = true;
      let errorMsg: string | undefined = undefined;

      if (!matchedConfig) {
        isValid = false;
        errorMsg = `El código "${rawCode}" no pertenece a la ${UNIT_INDICATORS_CONFIG[targetDept]?.unitName}.`;
        result.warnings.push(errorMsg);
      } else if (isNaN(valor)) {
        isValid = false;
        errorMsg = `El valor reportado para ${rawCode} no es un número válido.`;
      } else if (valor < 0) {
        isValid = false;
        errorMsg = `El valor reportado para ${rawCode} no puede ser negativo.`;
      }

      result.items.push({
        indicador_codigo: matchedConfig ? matchedConfig.codigo : rawCode,
        indicador_nombre: nombre || rawCode,
        unidad_medida: unidad,
        meta_periodo: isNaN(meta) ? 0 : meta,
        valor_registrado: isNaN(valor) ? 0 : valor,
        observaciones: obs || `Importado vía Excel: ${file.name}`,
        isValid,
        error: errorMsg,
      });

      result.totalRows++;
      if (isValid) {
        result.validRows++;
      }
    }

    if (result.validRows === 0) {
      result.errors.push('No se encontraron filas con indicadores oficiales válidos para cargar.');
    } else {
      result.success = true;
    }

    // Comprobar indicadores faltantes
    const loadedCodes = new Set(result.items.filter((r) => r.isValid).map((r) => r.indicador_codigo));
    for (const expected of validConfigs) {
      if (!loadedCodes.has(expected.codigo)) {
        result.warnings.push(`Indicador pendiente: ${expected.codigo} (${expected.nombre}) no vino en el archivo.`);
      }
    }

    return result;
  } catch (err: any) {
    result.errors.push(`Error crítico al leer el archivo Excel: ${err.message || String(err)}`);
    return result;
  }
}
