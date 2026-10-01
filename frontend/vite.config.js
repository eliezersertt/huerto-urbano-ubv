import tailwindcss from '@tailwindcss/vite'
import vue from '@vitejs/plugin-vue'
import { defineConfig } from 'vite'

// https://vite.dev/config/
// La URL del backend se inyecta con VITE_API_URL (ver src/lib/api.js).
// No hay proxy: el mismo codigo sirve en local y en la nube.
export default defineConfig({
  plugins: [vue(), tailwindcss()],
})
