<script setup>
import { ref } from 'vue'

// Ruta del logo oficial. Colócalo en frontend/public/logo-ubv.png
const logoPath = '/logo-ubv.png'
const logoFailed = ref(false)

const values = [
  {
    title: 'Agroecología',
    text: 'Cultivamos en equilibrio con el suelo y la vida, sin agredir el territorio.',
    icon: 'M12 2C7 6 5 10 5 14a7 7 0 0 0 14 0c0-4-2-8-7-12Zm0 18a4 4 0 0 1-4-4c0-2.5 1.5-5 4-7 2.5 2 4 4.5 4 7a4 4 0 0 1-4 4Z',
  },
  {
    title: 'Soberanía alimentaria',
    text: 'Producimos alimentos sanos y cercanos para nuestra comunidad universitaria.',
    icon: 'M12 3v6m0 0a4 4 0 0 0-4 4v2a4 4 0 0 0 8 0v-2a4 4 0 0 0-4-4Zm-8 7v2m16-2v2M12 21v-2',
  },
  {
    title: 'Saberes compartidos',
    text: 'Aprendemos haciendo: el huerto es aula, laboratorio y lugar de encuentro.',
    icon: 'M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8Zm13 10v-2a4 4 0 0 0-3-3.87M15 3.13a4 4 0 0 1 0 7.75',
  },
]
</script>

<template>
  <main>
    <section class="bg-ubv text-white">
      <div class="mx-auto w-full max-w-lg px-5 py-16 text-center">
        <div
          class="mx-auto flex h-48 w-48 items-center justify-center overflow-hidden rounded-full ring-1 ring-white/25 sm:h-60 sm:w-60"
        >
          <img
            v-if="!logoFailed"
            :src="logoPath"
            alt="Logo de la Universidad Bolivariana de Venezuela"
            class="h-full w-full object-cover"
            @error="logoFailed = true"
          />
          <span v-else class="font-display text-4xl font-medium text-white/90">UBV</span>
        </div>

        <p class="mt-6 text-sm text-white/75">Universidad Bolivariana de Venezuela</p>

        <h1 class="mt-3 font-display text-4xl font-medium leading-tight">
          La Casa de los Saberes
        </h1>

        <p class="mx-auto mt-4 max-w-sm text-base text-white/85">
          Un huerto universitario dedicado a la agroecología y al desarrollo sustentable.
        </p>

        <RouterLink
          to="/censo"
          class="mt-8 inline-flex items-center justify-center gap-2 rounded-full bg-leaf px-7 py-3.5 text-base font-semibold text-white shadow-soft transition-colors duration-200 hover:bg-leaf-deep focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-leaf"
        >
          <svg class="h-5 w-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true">
            <path d="M12 3v6m0 0a4 4 0 0 0-4 4v2a4 4 0 0 0 8 0v-2a4 4 0 0 0-4-4Z" stroke-linecap="round" stroke-linejoin="round" />
          </svg>
          Explorar el Censo Arbóreo
        </RouterLink>
      </div>
    </section>

    <section class="mx-auto w-full max-w-lg px-5 py-14">
      <p class="text-sm font-medium text-ubv">Quiénes somos</p>
      <h2 class="mt-2 font-display text-3xl font-medium leading-tight text-ubv-deep">
        El huerto como proyecto de vida
      </h2>
      <p class="mt-4 text-base leading-relaxed text-slate">
        Somos la comunidad de la Universidad Bolivariana de Venezuela. En este huerto
        urbano unimos la docencia, la investigación y la producción, sembrando valores
        que sostienen a nuestra casa de estudios y a su entorno.
      </p>

      <div class="mt-8 space-y-4">
        <article
          v-for="value in values"
          :key="value.title"
          class="flex gap-4 rounded-2xl border border-line bg-card p-5 shadow-card"
        >
          <span
            class="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl bg-sage text-leaf"
            aria-hidden="true"
          >
            <svg class="h-5 w-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6">
              <path :d="value.icon" stroke-linecap="round" stroke-linejoin="round" />
            </svg>
          </span>
          <div>
            <h3 class="font-display text-lg font-medium text-ink">{{ value.title }}</h3>
            <p class="mt-1 text-sm leading-relaxed text-slate">{{ value.text }}</p>
          </div>
        </article>
      </div>
    </section>
  </main>
</template>
