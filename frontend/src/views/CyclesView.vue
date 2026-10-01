<script setup>
const phases = [
  { day: 'Día 1', title: 'Siembra', detail: 'Semillas en bandejas de germinación' },
  { day: 'Día 7', title: 'Germinación', detail: 'Primeros brotes visibles' },
  { day: 'Día 14', title: 'Trasplante', detail: 'Paso a camas de cultivo' },
  { day: 'Día 30', title: 'Riego y abono', detail: 'Riego por goteo cada 3 días' },
  { day: 'Día 60', title: 'Cosecha', detail: 'Recolección manual' },
]

const week = [
  { day: 'Lun', action: 'Riego', active: true },
  { day: 'Mar', action: '—', active: false },
  { day: 'Mié', action: 'Riego', active: true },
  { day: 'Jue', action: '—', active: false },
  { day: 'Vie', action: 'Abono', active: true },
  { day: 'Sáb', action: '—', active: false },
  { day: 'Dom', action: 'Riego', active: true },
]
</script>

<template>
  <main class="mx-auto w-full max-w-lg px-5 py-10">
    <header>
      <p class="text-sm font-medium text-leaf">Gestión interna</p>
      <h1 class="mt-2 font-display text-4xl font-medium leading-tight text-leaf-deep">
        Ciclos y Horarios
      </h1>
      <p class="mt-2 max-w-sm text-base text-moss">
        Fases del cultivo y calendario semanal de cuidados.
      </p>
    </header>

    <section class="mt-8">
      <h2 class="font-display text-lg font-medium text-leaf-deep">Ciclo actual</h2>

      <ol class="relative mt-4 ml-2 space-y-6 border-l border-line pl-6">
        <li v-for="phase in phases" :key="phase.day" class="relative">
          <span
            class="absolute -left-[31px] top-1 h-2.5 w-2.5 rounded-full bg-leaf ring-4 ring-paper"
            aria-hidden="true"
          ></span>
          <p class="text-xs font-medium uppercase tracking-wide text-moss">{{ phase.day }}</p>
          <p class="mt-0.5 font-display text-base text-ink">{{ phase.title }}</p>
          <p class="mt-0.5 text-sm text-moss">{{ phase.detail }}</p>
        </li>
      </ol>
    </section>

    <section class="mt-10 rounded-3xl border border-line bg-card p-6 shadow-soft">
      <h2 class="font-display text-lg font-medium text-leaf-deep">Riego semanal</h2>
      <p class="mt-1 text-sm text-moss">Patrón recomendado para la parcela sur.</p>

      <div class="mt-5 grid grid-cols-7 gap-2">
        <div
          v-for="entry in week"
          :key="entry.day"
          class="flex flex-col items-center gap-1.5 rounded-xl py-2.5"
          :class="entry.active ? 'bg-sage' : 'bg-paper'"
        >
          <span class="text-xs text-moss">{{ entry.day }}</span>
          <span
            class="h-2 w-2 rounded-full"
            :class="entry.active ? 'bg-leaf' : 'bg-line'"
            aria-hidden="true"
          ></span>
          <span class="text-[10px] leading-none text-moss">{{ entry.action }}</span>
        </div>
      </div>
    </section>
  </main>
</template>
