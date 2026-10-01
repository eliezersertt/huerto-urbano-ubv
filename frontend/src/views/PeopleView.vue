<script setup>
const people = [
  { name: 'Lisbeth Gallardo', role: 'Coordinadora', area: 'Censo arbóreo', initials: 'LG' },
  { name: 'María Pérez', role: 'Encargada', area: 'Semilleros', initials: 'MP' },
  { name: 'José Rojas', role: 'Voluntario', area: 'Riego y horarios', initials: 'JR' },
  { name: 'Ana Torres', role: 'Voluntaria', area: 'Inventario', initials: 'AT' },
  { name: 'Carlos Medina', role: 'Voluntario', area: 'Cosecha', initials: 'CM' },
  { name: 'Rosa Núñez', role: 'Voluntaria', area: 'Meliponicultura', initials: 'RN' },
]
</script>

<template>
  <main class="mx-auto w-full max-w-lg px-5 py-10">
    <header>
      <p class="text-sm font-medium text-leaf">Gestión interna</p>
      <h1 class="mt-2 font-display text-4xl font-medium leading-tight text-leaf-deep">
        Responsables
      </h1>
      <p class="mt-2 max-w-sm text-base text-moss">
        Equipo del huerto y sus áreas de trabajo.
      </p>
    </header>

    <div class="mt-8 grid grid-cols-1 gap-3">
      <article
        v-for="person in people"
        :key="person.name"
        class="flex items-center gap-4 rounded-2xl border border-line bg-card p-4 shadow-card"
      >
        <span
          class="flex h-12 w-12 shrink-0 items-center justify-center rounded-full bg-leaf/[0.08] font-display text-base font-medium text-leaf ring-1 ring-leaf/20"
          aria-hidden="true"
        >
          {{ person.initials }}
        </span>

        <div class="min-w-0 flex-1">
          <p class="truncate font-display text-base text-ink">{{ person.name }}</p>
          <p class="text-sm text-moss">{{ person.role }}</p>
        </div>

        <span class="shrink-0 rounded-full bg-sage px-2.5 py-1 text-xs font-medium text-leaf-deep">
          {{ person.area }}
        </span>
      </article>
    </div>
  </main>
</template>
