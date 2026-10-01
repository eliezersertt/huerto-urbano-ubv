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
    if (response.status === 404) throw new Error('Esta placa no está en el censo')
    if (!response.ok) throw new Error('No se pudo cargar la ficha')
    plant.value = await response.json()
  } catch (e) {
    error.value = e.message || 'Sin conexión con el servidor'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <main class="min-h-screen bg-paper text-ink">
    <div class="mx-auto w-full max-w-lg px-5 py-8">
      <RouterLink
        to="/"
        class="inline-flex items-center gap-1.5 rounded-full border border-leaf/30 bg-card px-4 py-2 text-sm font-medium text-leaf transition-colors duration-200 hover:bg-leaf hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-leaf"
      >
        <svg
          class="h-4 w-4"
          viewBox="0 0 16 16"
          fill="none"
          stroke="currentColor"
          stroke-width="1.5"
          aria-hidden="true"
        >
          <path d="M10 3 5 8l5 5" stroke-linecap="round" stroke-linejoin="round" />
        </svg>
        Volver al listado
      </RouterLink>

      <p v-if="loading" class="mt-10 text-center text-sm text-moss">
        Cargando la ficha...
      </p>

      <p
        v-else-if="error"
        class="mt-10 rounded-xl border border-seed/30 bg-seed/10 p-4 text-sm text-leaf-deep"
      >
        {{ error }}
      </p>

      <template v-else-if="plant">
        <header class="mt-6">
          <div class="flex items-center gap-3">
            <span
              class="flex h-11 w-11 items-center justify-center rounded-full border border-leaf/35 bg-leaf/[0.06] font-display text-base font-medium text-leaf"
            >
              {{ plant.census_number }}
            </span>
            <span class="text-sm font-medium text-moss">Placa del ejemplar</span>
          </div>

          <h1 class="mt-4 font-display text-3xl font-medium leading-tight text-leaf-deep">
            {{ plant.common_name || 'Ejemplar sin nombre' }}
          </h1>
          <p v-if="plant.scientific_name" class="mt-1 text-base italic text-moss">
            {{ plant.scientific_name }}
          </p>
        </header>

        <dl class="mt-7 grid grid-cols-2 gap-px overflow-hidden rounded-2xl border border-line bg-line">
          <div v-if="plant.origin" class="bg-card p-4">
            <dt class="text-xs text-moss">Origen</dt>
            <dd class="mt-1 text-sm font-medium text-ink">{{ plant.origin }}</dd>
          </div>
          <div v-if="plant.dap" class="bg-card p-4">
            <dt class="text-xs text-moss">Diámetro (DAP)</dt>
            <dd class="mt-1 text-sm font-medium text-ink">{{ plant.dap }} cm</dd>
          </div>
          <div v-if="plant.trunk_shape" class="bg-card p-4">
            <dt class="text-xs text-moss">Forma del fuste</dt>
            <dd class="mt-1 text-sm font-medium text-ink">{{ plant.trunk_shape }}</dd>
          </div>
          <div v-if="plant.height" class="bg-card p-4">
            <dt class="text-xs text-moss">Altura</dt>
            <dd class="mt-1 text-sm font-medium text-ink">{{ plant.height }} m</dd>
          </div>
        </dl>

        <section class="mt-8 rounded-3xl border border-line bg-card p-7 text-center shadow-soft">
          <h2 class="font-display text-xl font-medium text-leaf-deep">Código QR</h2>
          <p class="mt-1 text-sm text-moss">Escanea para abrir esta ficha.</p>

          <div class="mt-5 inline-block rounded-2xl border border-line bg-white p-4">
            <img
              :src="qrUrl"
              alt="Código QR del ejemplar"
              class="h-52 w-52"
            />
          </div>
        </section>
      </template>
    </div>
  </main>
</template>
