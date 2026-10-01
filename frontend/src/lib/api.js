// Base URL del backend.
// Siempre viene de VITE_API_URL, para que cada entorno (local, Vercel)
// inyecte su propio valor sin tocar el codigo.
const RAW_API_URL = import.meta.env.VITE_API_URL ?? ''

export const API_URL = RAW_API_URL.replace(/\/$/, '')

export function apiUrl(path) {
  return `${API_URL}${path}`
}
