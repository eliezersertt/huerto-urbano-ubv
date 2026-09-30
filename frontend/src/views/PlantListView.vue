<script setup>
import { onMounted, ref } from 'vue'

const plants = ref([])
const loading = ref(true)
const error = ref('')

onMounted(async () => {
  try {
    const response = await fetch('/api/plants')
    if (!response.ok) throw new Error('Error al cargar las plantas')
    plants.value = await response.json()
  } catch (e) {
    error.value = e.message || 'Sin conexión con el servidor'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <main class="min-h-screen bg-green-50 px-4 py-6">
    <div class="mx-auto w-full max-w-md">
      <header class="mb-6 text-center">
        <h1 class="text-2xl font-bold text-green-800">Huerto Urbano</h1>
        <p class="mt-1 text-sm text-green-700">Censo arbóreo</p>
      </header>

      <p v-if="loading" class="text-center text-sm text-gray-500">
        Cargando plantas...
      </p>

      <p v-else-if="error" class="rounded-lg bg-red-100 p-3 text-sm text-red-700">
        {{ error }}
      </p>

      <ul v-else class="space-y-3">
        <li v-for="plant in plants" :key="plant.id">
          <RouterLink
            :to="`/planta/${plant.census_number}`"
            class="block rounded-xl bg-white p-4 shadow"
          >
            <div class="flex items-start justify-between gap-2">
              <div>
                <p class="font-semibold text-gray-800">
                  {{ plant.common_name || 'Sin nombre' }}
                </p>
                <p class="text-sm italic text-gray-500">
                  {{ plant.scientific_name || 'Sin especie' }}
                </p>
              </div>
              <span class="rounded-full bg-green-100 px-2 py-1 text-xs font-medium text-green-800">
                N.º {{ plant.census_number }}
              </span>
            </div>
            <p v-if="plant.height" class="mt-2 text-sm text-gray-600">
              Altura: {{ plant.height }} m
            </p>
          </RouterLink>
        </li>
      </ul>

      <p v-if="!loading && !error && plants.length === 0" class="text-center text-sm text-gray-500">
        No hay plantas registradas.
      </p>
    </div>
  </main>
</template>
