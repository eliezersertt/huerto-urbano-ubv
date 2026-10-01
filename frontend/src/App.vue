<script setup>
import AppNavbar from './components/AppNavbar.vue'
</script>

<template>
  <div class="min-h-screen bg-paper text-ink">
    <AppNavbar />
    <RouterView />
  </div>
</template>
