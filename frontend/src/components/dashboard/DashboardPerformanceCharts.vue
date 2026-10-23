<script setup lang="ts">
withDefaults(
  defineProps<{
    globalCompliance?: number;
  }>(),
  {
    globalCompliance: 94.2,
  }
);
</script>

<template>
  <section class="grid grid-cols-1 lg:grid-cols-[2.2fr_1fr] gap-3.5">
    <!-- Curva Temporal SVG -->
    <div class="bg-white border border-ash rounded-[3px] p-5 flex flex-col justify-between">
      <div class="flex items-start justify-between mb-4">
        <div>
          <h3 class="text-base font-semibold text-ink-black">
            Evolución Histórica de Cumplimiento Mensual (2026)
          </h3>
          <p class="text-xs font-normal text-steel">
            Comportamiento agregado de las 5 unidades de estadística del INE Monagas
          </p>
        </div>
        <span class="text-xs font-semibold px-2 py-0.5 bg-signal-blue/10 text-signal-blue border border-signal-blue/25 rounded-[3px]">
          Tendencia Positiva
        </span>
      </div>

      <div class="w-full">
        <svg viewBox="0 0 700 200" class="w-full h-[180px] max-md:h-[140px]">
          <line x1="40" y1="30" x2="680" y2="30" stroke="#f0f0f0" stroke-dasharray="4" />
          <line x1="40" y1="80" x2="680" y2="80" stroke="#f0f0f0" stroke-dasharray="4" />
          <line x1="40" y1="130" x2="680" y2="130" stroke="#f0f0f0" stroke-dasharray="4" />
          <line x1="40" y1="180" x2="680" y2="180" stroke="#d1d4d5" />

          <text x="10" y="34" font-size="11" font-weight="600" fill="#424647">100%</text>
          <text x="15" y="84" font-size="11" font-weight="600" fill="#424647">80%</text>
          <text x="15" y="134" font-size="11" font-weight="600" fill="#424647">60%</text>

          <polygon
            points="80,140 180,120 280,105 380,95 480,75 580,50 580,180 80,180"
            fill="rgba(39, 73, 255, 0.08)"
          />

          <polyline
            fill="none"
            stroke="#2749ff"
            stroke-width="2.5"
            stroke-linecap="round"
            stroke-linejoin="round"
            points="80,140 180,120 280,105 380,95 480,75 580,50"
          />

          <circle cx="80" cy="140" r="4" fill="#ffffff" stroke="#2749ff" stroke-width="2" />
          <text x="70" y="195" font-size="11" font-weight="500" fill="#424647">Mar</text>

          <circle cx="180" cy="120" r="4" fill="#ffffff" stroke="#2749ff" stroke-width="2" />
          <text x="170" y="195" font-size="11" font-weight="500" fill="#424647">Abr</text>

          <circle cx="280" cy="105" r="4" fill="#ffffff" stroke="#2749ff" stroke-width="2" />
          <text x="270" y="195" font-size="11" font-weight="500" fill="#424647">May</text>

          <circle cx="380" cy="95" r="4" fill="#ffffff" stroke="#2749ff" stroke-width="2" />
          <text x="370" y="195" font-size="11" font-weight="500" fill="#424647">Jun</text>

          <circle cx="480" cy="75" r="4" fill="#ffffff" stroke="#2749ff" stroke-width="2" />
          <text x="470" y="195" font-size="11" font-weight="500" fill="#424647">Jul</text>

          <circle cx="580" cy="50" r="5" fill="#2749ff" stroke="#ffffff" stroke-width="2" />
          <text x="545" y="195" font-size="12" font-weight="600" fill="#000000">Ago ({{ globalCompliance }}%)</text>
        </svg>
      </div>
    </div>

    <!-- Medidor Radial Donut SVG -->
    <div class="bg-white border border-ash rounded-[3px] p-5 flex flex-col justify-between items-center text-center">
      <div class="w-full text-left mb-2">
        <h3 class="text-base font-semibold text-ink-black">Eficiencia Operativa</h3>
        <p class="text-xs font-normal text-steel">Meta vs Ejecución Real Agosto</p>
      </div>

      <div class="w-36 h-36 my-2">
        <svg viewBox="0 0 160 160" class="w-full h-full">
          <circle
            cx="80"
            cy="80"
            r="65"
            fill="none"
            stroke="#ededed"
            stroke-width="12"
          />
          <circle
            cx="80"
            cy="80"
            r="65"
            fill="none"
            stroke="#2749ff"
            stroke-width="12"
            stroke-dasharray="408"
            stroke-dashoffset="24"
            stroke-linecap="round"
            transform="rotate(-90 80 80)"
          />
          <text x="80" y="76" text-anchor="middle" font-size="26" fill="#000000" font-weight="600">{{ globalCompliance }}%</text>
          <text x="80" y="96" text-anchor="middle" font-size="11" fill="#424647" font-weight="600">CUMPLIMIENTO</text>
        </svg>
      </div>

      <div class="w-full pt-2 border-t border-mist">
        <span class="inline-flex items-center px-2 py-0.5 text-xs font-semibold bg-mist text-ink-black rounded-[3px]">
          33 de 35 Indicadores en Meta
        </span>
      </div>
    </div>
  </section>
</template>
