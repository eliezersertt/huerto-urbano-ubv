<script setup>
const items = [
  { name: 'Pala de mano', category: 'Herramienta', quantity: 12, unit: 'unidades', status: 'Disponible' },
  { name: 'Rastrillo', category: 'Herramienta', quantity: 8, unit: 'unidades', status: 'Disponible' },
  { name: 'Abono orgánico', category: 'Insumo', quantity: 24, unit: 'sacos', status: 'Nivel bajo' },
  { name: 'Regadera', category: 'Herramienta', quantity: 6, unit: 'unidades', status: 'Disponible' },
  { name: 'Sustrato', category: 'Insumo', quantity: 40, unit: 'sacos', status: 'Disponible' },
  { name: 'Guantes', category: 'Protección', quantity: 15, unit: 'pares', status: 'Disponible' },
  { name: 'Tijeras de poda', category: 'Herramienta', quantity: 4, unit: 'unidades', status: 'Disponible' },
  { name: 'Semillas mixtas', category: 'Insumo', quantity: 9, unit: 'sobres', status: 'Nivel bajo' },
]
</script>

<template>
  <main class="mx-auto w-full max-w-lg px-5 py-10">
    <header>
      <p class="text-sm font-medium text-leaf">Gestión interna</p>
      <h1 class="mt-2 font-display text-4xl font-medium leading-tight text-leaf-deep">
        Inventario
      </h1>
      <p class="mt-2 max-w-sm text-base text-moss">
        Herramientas e insumos disponibles para el cuidado del huerto.
      </p>
    </header>

    <div class="mt-8 grid grid-cols-1 gap-3">
      <article
        v-for="item in items"
        :key="item.name"
        class="flex items-center gap-4 rounded-2xl border border-line bg-card p-4 shadow-card"
      >
        <span
          class="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl bg-sage text-leaf"
          aria-hidden="true"
        >
          <svg class="h-5 w-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6">
            <path d="M12 3v8m0 0H5a3 3 0 0 0 0 6h3m4-6v8m0-8h7a3 3 0 0 1 0 6h-3" stroke-linecap="round" stroke-linejoin="round" />
          </svg>
        </span>

        <div class="min-w-0 flex-1">
          <p class="truncate font-display text-base text-ink">{{ item.name }}</p>
          <p class="text-xs text-moss">{{ item.category }}</p>
        </div>

        <div class="text-right">
          <p class="font-display text-xl font-medium text-leaf-deep">{{ item.quantity }}</p>
          <p class="text-xs text-moss">{{ item.unit }}</p>
        </div>

        <span
          class="shrink-0 rounded-full px-2.5 py-1 text-xs font-medium"
          :class="
            item.status === 'Disponible'
              ? 'bg-sage text-leaf-deep'
              : 'bg-seed/15 text-seed'
          "
        >
          {{ item.status }}
        </span>
      </article>
    </div>
  </main>
</template>
