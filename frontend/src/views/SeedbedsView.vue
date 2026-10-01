<script setup>
const seedbeds = [
  { name: 'Bandeja 01', species: 'Lechuga', progress: 80, planted: '12 sep', stage: 'Trasplante' },
  { name: 'Bandeja 02', species: 'Tomate', progress: 35, planted: '20 sep', stage: 'Germinando' },
  { name: 'Bandeja 03', species: 'Albahaca', progress: 60, planted: '15 sep', stage: 'Crecimiento' },
  { name: 'Bandeja 04', species: 'Cilantro', progress: 15, planted: '28 sep', stage: 'Siembra' },
  { name: 'Bandeja 05', species: 'Perejil', progress: 48, planted: '18 sep', stage: 'Crecimiento' },
  { name: 'Bandeja 06', species: 'Pimiento', progress: 22, planted: '25 sep', stage: 'Germinando' },
]
</script>

<template>
  <main class="mx-auto w-full max-w-lg px-5 py-10">
    <header>
      <p class="text-sm font-medium text-ubv">Gestión interna</p>
      <h1 class="mt-2 font-display text-4xl font-medium leading-tight text-ubv-deep">
        Semilleros
      </h1>
      <p class="mt-2 max-w-sm text-base text-slate">
        Estado de germinación de las bandejas en vivero.
      </p>
    </header>

    <div class="mt-8 grid grid-cols-1 gap-3">
      <article
        v-for="bed in seedbeds"
        :key="bed.name"
        class="rounded-2xl border border-line bg-card p-5 shadow-card"
      >
        <div class="flex items-center justify-between">
          <p class="font-display text-base text-ink">{{ bed.name }}</p>
          <span class="rounded-full bg-sage px-2.5 py-1 text-xs font-medium text-leaf-deep">
            {{ bed.stage }}
          </span>
        </div>

        <p class="mt-1 text-sm text-slate">
          {{ bed.species }} · sembrado el {{ bed.planted }}
        </p>

        <div class="mt-4 flex items-center gap-3">
          <div class="h-2 flex-1 overflow-hidden rounded-full bg-sage">
            <div
              class="h-full rounded-full bg-leaf transition-all"
              :style="{ width: bed.progress + '%' }"
            ></div>
          </div>
          <span class="font-display text-sm font-medium text-ubv-deep">
            {{ bed.progress }}%
          </span>
        </div>
      </article>
    </div>
  </main>
</template>
