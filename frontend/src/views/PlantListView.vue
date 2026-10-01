<script setup>
import { computed, onMounted, ref } from 'vue'

const plants = ref([])
const loading = ref(true)
const error = ref('')

const total = computed(() => plants.value.length)

onMounted(async () => {
  try {
    const response = await fetch('/api/plants')
    if (!response.ok) throw new Error('No se pudieron cargar las plantas')
    plants.value = await response.json()
  } catch (e) {
    error.value = e.message || 'Sin conexión con el servidor'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <main class="mx-auto w-full max-w-lg px-5 py-10">
    <header>
      <p class="text-sm font-medium text-ubv">Censo · Parcela sur</p>
      <h1 class="mt-2 font-display text-4xl font-medium leading-tight text-ubv-deep">
        Censo Arbóreo
      </h1>
      <p class="mt-2 max-w-sm text-base text-slate">
        Escanea una placa física para abrir la ficha de cada ejemplar.
      </p>

      <div class="mt-6 flex items-baseline gap-3 border-t border-line pt-5">
        <span class="font-display text-5xl font-medium text-ubv">{{ total }}</span>
        <span class="text-sm text-slate">ejemplares registrados</span>
      </div>
    </header>

    <p v-if="loading" class="mt-10 text-center text-sm text-slate">
      Cargando el censo...
    </p>

    <p
      v-else-if="error"
      class="mt-10 rounded-xl border border-seed/30 bg-seed/10 p-4 text-sm text-ink"
    >
      {{ error }}
    </p>

    <ol v-else class="mt-8 divide-y divide-line">
      <li v-for="plant in plants" :key="plant.id">
        <RouterLink
          :to="`/planta/${plant.census_number}`"
          class="group -mx-3 flex items-center gap-4 rounded-2xl px-3 py-4 transition-colors duration-200 hover:bg-mist focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ubv"
        >
          <span
            class="flex h-12 w-12 shrink-0 items-center justify-center rounded-full border border-ubv/30 bg-ubv/[0.06] font-display text-lg font-medium text-ubv transition-transform duration-200 motion-reduce:transition-none group-hover:scale-105 motion-reduce:group-hover:scale-100"
          >
            {{ plant.census_number }}
          </span>

          <span class="min-w-0 flex-1">
            <span class="block truncate font-display text-lg text-ink">
              {{ plant.common_name || 'Sin nombre' }}
            </span>
            <span class="block truncate text-sm italic text-slate">
              {{ plant.scientific_name || 'Especie sin registrar' }}
            </span>
          </span>

          <span v-if="plant.height" class="shrink-0 text-sm text-slate">
            {{ plant.height }} m
          </span>
        </RouterLink>
      </li>
    </ol>

    <p
      v-if="!loading && !error && plants.length === 0"
      class="mt-10 text-center text-sm text-slate"
    >
      Aún no hay ejemplares registrados.
    </p>
  </main>
</template>
