import uuid
from typing import List, Dict, Any, Optional
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.models.measurement import IndicatorMeasurement
from app.models.version import MeasurementVersion

class VersioningService:
    @staticmethod
    def get_measurement_versions(db: Session, measurement_id: uuid.UUID) -> List[MeasurementVersion]:
        """
        Obtiene el historial completo de versiones de una medición, ordenado de la más reciente a la más antigua.
        """
        return (
            db.query(MeasurementVersion)
            .filter(MeasurementVersion.medicion_id == measurement_id)
            .order_by(MeasurementVersion.numero_version.desc())
            .all()
        )

    @staticmethod
    def rollback_measurement_version(
        db: Session,
        measurement_id: uuid.UUID,
        target_version: int,
        user_id: uuid.UUID,
        reason: str
    ) -> Dict[str, Any]:
        """
        Revierte una medición a una versión histórica anterior utilizando la función nativa de PostgreSQL.
        Garantiza que la reversión genere un nuevo snapshot auditable sin destruir el historial previo.
        """
        query = text("""
            SELECT fn_revertir_medicion(
                :medicion_id,
                :version_destino,
                :usuario_id,
                :motivo
            ) AS result;
        """)
        
        result = db.execute(
            query,
            {
                "medicion_id": str(measurement_id),
                "version_destino": target_version,
                "usuario_id": str(user_id),
                "motivo": reason
            }
        ).scalar()
        
        db.commit()
        return result

    @staticmethod
    def get_version_diff(
        db: Session,
        measurement_id: uuid.UUID,
        version_from: int,
        version_to: int
    ) -> Dict[str, Any]:
        """
        Compara dos versiones de una misma medición para diagnosticar qué causó la variación en las estadísticas.
        """
        v1 = (
            db.query(MeasurementVersion)
            .filter(
                MeasurementVersion.medicion_id == measurement_id,
                MeasurementVersion.numero_version == version_from
            )
            .first()
        )
        v2 = (
            db.query(MeasurementVersion)
            .filter(
                MeasurementVersion.medicion_id == measurement_id,
                MeasurementVersion.numero_version == version_to
            )
            .first()
        )

        if not v1 or not v2:
            raise ValueError("Una o ambas versiones especificadas no existen para esta medición.")

        diff = {
            "medicion_id": str(measurement_id),
            "version_base": version_from,
            "version_comparada": version_to,
            "diferencias": {
                "valor_registrado": {
                    "anterior": float(v1.valor_registrado),
                    "nuevo": float(v2.valor_registrado),
                    "delta": float(v2.valor_registrado - v1.valor_registrado)
                },
                "meta_periodo": {
                    "anterior": float(v1.meta_periodo) if v1.meta_periodo is not None else None,
                    "nuevo": float(v2.meta_periodo) if v2.meta_periodo is not None else None,
                },
                "estado": {
                    "anterior": v1.estado,
                    "nuevo": v2.estado
                },
                "motivo_cambio": v2.motivo_cambio,
                "modificado_por": str(v2.modificado_por) if v2.modificado_por else None,
                "fecha_cambio": v2.created_at.isoformat() if v2.created_at else None
            }
        }
        return diff
