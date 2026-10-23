<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';

const canvasRef = ref<HTMLCanvasElement | null>(null);

interface Node {
  x: number;
  y: number;
  vx: number;
  vy: number;
  radius: number;
  isHub: boolean;
  pulsePhase: number;
  color: string;
}

interface Pulse {
  fromNode: number;
  toNode: number;
  progress: number;
  speed: number;
}

let animationFrameId: number | null = null;
let nodes: Node[] = [];
let pulses: Pulse[] = [];
let mouse = { x: -1000, y: -1000, active: false };
let isVisible = true;

const colors = [
  '#2749ff', // Signal Blue
  '#15803d', // Eco Green
  '#4338ca', // Segen Indigo
  '#424647', // Steel
];

const initNodes = (width: number, height: number) => {
  const isMobile = width < 768;
  const count = isMobile ? 24 : 52;
  nodes = [];
  pulses = [];

  for (let i = 0; i < count; i++) {
    const isHub = i % 7 === 0;
    nodes.push({
      x: Math.random() * width,
      y: Math.random() * height,
      vx: (Math.random() - 0.5) * 0.45,
      vy: (Math.random() - 0.5) * 0.45,
      radius: isHub ? (isMobile ? 2.8 : 3.5) : (isMobile ? 1.5 : 2.0),
      isHub,
      pulsePhase: Math.random() * Math.PI * 2,
      color: isHub ? '#2749ff' : (colors[i % colors.length] || '#424647')
    });
  }
};

const handleResize = () => {
  if (!canvasRef.value) return;
  const canvas = canvasRef.value;
  const width = window.innerWidth;
  const height = window.innerHeight;
  const dpr = Math.min(window.devicePixelRatio || 1, 2);

  canvas.width = width * dpr;
  canvas.height = height * dpr;
  canvas.style.width = `${width}px`;
  canvas.style.height = `${height}px`;

  const ctx = canvas.getContext('2d');
  if (ctx) {
    ctx.scale(dpr, dpr);
  }

  initNodes(width, height);
};

const handleMouseMove = (e: MouseEvent) => {
  mouse.x = e.clientX;
  mouse.y = e.clientY;
  mouse.active = true;
};

const handleMouseLeave = () => {
  mouse.active = false;
};

const handleVisibilityChange = () => {
  isVisible = !document.hidden;
};

const animate = () => {
  if (!isVisible || !canvasRef.value) {
    animationFrameId = requestAnimationFrame(animate);
    return;
  }

  const canvas = canvasRef.value;
  const ctx = canvas.getContext('2d');
  if (!ctx) return;

  const width = window.innerWidth;
  const height = window.innerHeight;

  ctx.clearRect(0, 0, width, height);

  const maxDist = width < 768 ? 95 : 135;
  const connections: [number, number, number][] = [];

  // Update & Draw Nodes
  for (let i = 0; i < nodes.length; i++) {
    const n = nodes[i];

    // Posición
    n.x += n.vx;
    n.y += n.vy;

    // Rebote suave en bordes
    if (n.x < 10) { n.x = 10; n.vx *= -1; }
    if (n.x > width - 10) { n.x = width - 10; n.vx *= -1; }
    if (n.y < 10) { n.y = 10; n.vy *= -1; }
    if (n.y > height - 10) { n.y = height - 10; n.vy *= -1; }

    // Interacción con mouse
    if (mouse.active) {
      const dx = mouse.x - n.x;
      const dy = mouse.y - n.y;
      const dist = Math.sqrt(dx * dx + dy * dy);
      if (dist < 140) {
        const force = (1 - dist / 140) * 0.4;
        n.x -= (dx / dist) * force;
        n.y -= (dy / dist) * force;
      }
    }

    // Dibujar nodo
    n.pulsePhase += 0.03;
    const pulseFactor = n.isHub ? Math.sin(n.pulsePhase) * 0.4 + 1 : 1;

    // Anillo exterior en hubs
    if (n.isHub) {
      ctx.beginPath();
      ctx.arc(n.x, n.y, n.radius * 3.2 * pulseFactor, 0, Math.PI * 2);
      ctx.strokeStyle = 'rgba(39, 73, 255, 0.16)';
      ctx.lineWidth = 1;
      ctx.stroke();

      ctx.beginPath();
      ctx.arc(n.x, n.y, n.radius * 1.8, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(39, 73, 255, 0.25)';
      ctx.fill();
    }

    // Centro del nodo
    ctx.beginPath();
    ctx.arc(n.x, n.y, n.radius, 0, Math.PI * 2);
    ctx.fillStyle = n.color;
    ctx.fill();

    // Calcular conexiones
    for (let j = i + 1; j < nodes.length; j++) {
      const n2 = nodes[j];
      const dx = n.x - n2.x;
      const dy = n.y - n2.y;
      const dist = Math.sqrt(dx * dx + dy * dy);

      if (dist < maxDist) {
        connections.push([i, j, dist]);
        const alpha = (1 - dist / maxDist) * 0.18;
        ctx.beginPath();
        ctx.moveTo(n.x, n.y);
        ctx.lineTo(n2.x, n2.y);
        ctx.strokeStyle = n.isHub || n2.isHub 
          ? `rgba(39, 73, 255, ${alpha * 1.5})` 
          : `rgba(209, 212, 213, ${alpha * 1.2})`;
        ctx.lineWidth = n.isHub || n2.isHub ? 1.0 : 0.75;
        ctx.stroke();
      }
    }
  }

  // Generar y mover pulsos de datos sobre conexiones
  if (connections.length > 0 && Math.random() < 0.05 && pulses.length < 8) {
    const conn = connections[Math.floor(Math.random() * connections.length)];
    pulses.push({
      fromNode: conn[0],
      toNode: conn[1],
      progress: 0,
      speed: 0.012 + Math.random() * 0.018
    });
  }

  // Dibujar pulsos
  for (let pIdx = pulses.length - 1; pIdx >= 0; pIdx--) {
    const p = pulses[pIdx];
    p.progress += p.speed;

    if (p.progress >= 1) {
      pulses.splice(pIdx, 1);
      continue;
    }

    const n1 = nodes[p.fromNode];
    const n2 = nodes[p.toNode];
    if (n1 && n2) {
      const px = n1.x + (n2.x - n1.x) * p.progress;
      const py = n1.y + (n2.y - n1.y) * p.progress;

      ctx.beginPath();
      ctx.arc(px, py, 2.2, 0, Math.PI * 2);
      ctx.fillStyle = '#2749ff';
      ctx.fill();
    }
  }

  animationFrameId = requestAnimationFrame(animate);
};

onMounted(() => {
  window.addEventListener('resize', handleResize);
  window.addEventListener('mousemove', handleMouseMove);
  window.addEventListener('mouseleave', handleMouseLeave);
  document.addEventListener('visibilitychange', handleVisibilityChange);

  handleResize();
  animationFrameId = requestAnimationFrame(animate);
});

onUnmounted(() => {
  window.removeEventListener('resize', handleResize);
  window.removeEventListener('mousemove', handleMouseMove);
  window.removeEventListener('mouseleave', handleMouseLeave);
  document.removeEventListener('visibilitychange', handleVisibilityChange);

  if (animationFrameId !== null) {
    cancelAnimationFrame(animationFrameId);
  }
});
</script>

<template>
  <div class="fixed inset-0 pointer-events-none overflow-hidden z-0 select-none">
    <!-- Trama geométrica de cuadrícula sutil -->
    <div 
      class="absolute inset-0 opacity-40 bg-[radial-gradient(#d1d4d5_1px,transparent_1px)] [background-size:28px_28px]"
    ></div>

    <!-- Gradiente radial de luz ambiental institucional -->
    <div class="absolute inset-0 bg-[radial-gradient(circle_at_50%_45%,rgba(255,255,255,0.92)_0%,rgba(245,245,247,0.7)_60%,rgba(237,237,237,0.85)_100%)]"></div>

    <!-- Canvas con red geométrica abstracta y dinámica -->
    <canvas 
      ref="canvasRef" 
      class="absolute inset-0 w-full h-full block"
    ></canvas>
  </div>
</template>
