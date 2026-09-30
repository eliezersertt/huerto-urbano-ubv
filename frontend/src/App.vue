<script setup>
import { onMounted, ref } from 'vue'

const apiStatus = ref('Comprobando...')

onMounted(async () => {
  try {
    const response = await fetch('/api/health')
    if (!response.ok) throw new Error('Sin respuesta')
    const data = await response.json()
    apiStatus.value = data.status === 'ok' ? 'Conectada' : 'Con errores'
  } catch {
    apiStatus.value = 'Desconectada'
  }
})
</script>

<template>
  <main class="min-h-screen bg-green-50 px-4 py-8">
    <div class="mx-auto w-full max-w-md">
      <header class="text-center">
        <h1 class="text-3xl font-bold text-green-800">Huerto Urbano</h1>
        <p class="mt-2 text-base text-green-700">
          Gestion del huerto universitario
        </p>
      </header>

      <section class="mt-8 rounded-xl bg-white p-5 shadow">
        <h2 class="text-lg font-semibold text-gray-800">Estado del sistema</h2>
        <p class="mt-2 text-sm text-gray-600">
          API:
          <span class="font-medium text-green-700">{{ apiStatus }}</span>
        </p>
      </section>

      <p class="mt-8 text-center text-xs text-gray-500">
        Version 0.1.0
      </p>
    </div>
  </main>
</template>
