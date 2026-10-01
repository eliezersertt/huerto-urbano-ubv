<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()

const items = [
  { label: 'Censo Arbóreo', to: '/' },
  { label: 'Inventario', to: '/inventario' },
  { label: 'Ciclos y Horarios', to: '/ciclos' },
  { label: 'Semilleros', to: '/semilleros' },
  { label: 'Responsables', to: '/responsables' },
]

function isActive(item) {
  if (item.to === '/') {
    return route.path === '/' || route.path.startsWith('/planta')
  }
  return route.path.startsWith(item.to)
}
</script>

<template>
  <header class="sticky top-0 z-10 border-b border-line bg-paper/85 backdrop-blur">
    <div class="mx-auto w-full max-w-lg px-5">
      <div class="flex items-center justify-between py-3">
        <RouterLink to="/" class="flex items-center gap-2 font-display text-lg font-medium text-leaf-deep">
          <svg class="h-5 w-5 text-leaf" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
            <path d="M12 2C7 6 5 10 5 14a7 7 0 0 0 14 0c0-4-2-8-7-12Zm0 18a4 4 0 0 1-4-4c0-2.5 1.5-5 4-7 2.5 2 4 4.5 4 7a4 4 0 0 1-4 4Z" />
          </svg>
          Huerto Urbano
        </RouterLink>
        <span class="text-xs text-moss">Jardín botánico</span>
      </div>

      <nav class="no-scrollbar -mx-1 flex gap-1.5 overflow-x-auto px-1 pb-3">
        <RouterLink
          v-for="item in items"
          :key="item.to"
          :to="item.to"
          class="whitespace-nowrap rounded-full px-3.5 py-1.5 text-sm transition-colors duration-200 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-leaf"
          :class="
            isActive(item)
              ? 'bg-leaf font-medium text-white'
              : 'text-moss hover:bg-sage'
          "
        >
          {{ item.label }}
        </RouterLink>
      </nav>
    </div>
  </header>
</template>
