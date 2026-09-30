<script setup>
import { computed, onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

const plant = ref(null)
const loading = ref(true)
const error = ref('')

const qrUrl = computed(() =>
  plant.value ? `/api/plants/${plant.value.id}/qr` : ''
)

onMounted(async () => {
  try {
    const response = await fetch(`/api/plants/census/${route.params.censusNumber}`)
    if (response.status === 404) throw new Error('Planta no encontrada')
    if (!response.ok) throw new Error('Error al cargar la planta')
    plant.value = await response.json()
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
      <RouterLink
        to="/"
        class="mb-4 inline-block text-sm text-green-700 underline"
      >
        Volver al listado
      </RouterLink>

      <p v-if="loading" class="text-center text-sm text-gray-500">
        Cargando...
      </p>

      <p v-else-if="error" class="rounded-lg bg-red-100 p-3 text-sm text-red-700">
        {{ error }}
      </p>

      <template v-else-if="plant">
        <section class="rounded-xl bg-white p-5 shadow">
          <div class="flex items-start justify-between gap-2">
            <h1 class="text-xl font-bold text-gray-800">
              {{ plant.common_name || 'Sin nombre' }}
            </h1>
            <span class="rounded-full bg-green-100 px-2 py-1 text-xs font-medium text-green-800">
              N.º {{ plant.census_number }}
            </span>
          </div>

          <dl class="mt-4 space-y-2 text-sm">
            <div v-if="plant.scientific_name">
              <dt class="text-gray-500">Nombre científico</dt>
              <dd class="italic text-gray-800">{{ plant.scientific_name }}</dd>
            </div>
            <div v-if="plant.origin">
              <dt class="text-gray-500">Origen</dt>
              <dd class="text-gray-800">{{ plant.origin }}</dd>
            </div>
            <div v-if="plant.dap">
              <dt class="text-gray-500">Diámetro (DAP)</dt>
              <dd class="text-gray-800">{{ plant.dap }} cm</dd>
            </div>
            <div v-if="plant.trunk_shape">
              <dt class="text-gray-500">Forma del fuste</dt>
              <dd class="text-gray-800">{{ plant.trunk_shape }}</dd>
            </div>
            <div v-if="plant.height">
              <dt class="text-gray-500">Altura</dt>
              <dd class="text-gray-800">{{ plant.height }} m</dd>
            </div>
          </dl>
        </section>

        <section class="mt-5 rounded-xl bg-white p-5 text-center shadow">
          <h2 class="text-base font-semibold text-gray-800">Código QR</h2>
          <p class="mt-1 text-xs text-gray-500">
            Escanéalo para abrir esta ficha.
          </p>
          <img
            :src="qrUrl"
            alt="Código QR de la planta"
            class="mx-auto mt-3 h-52 w-52"
          />
        </section>
      </template>
    </div>
  </main>
</template>
