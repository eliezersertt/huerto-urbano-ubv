# Bitácora del Proyecto: Huerto Urbano (PWA)

## 1. Descripción General
Aplicación web "Mobile-First" (PWA) para la gestión de un huerto universitario. Sirve para leer QR de plantas y como herramienta de gestión interna (tiempos agrícolas, inventarios, meliponicultura).

## 2. Stack Tecnológico
*   **Backend:** Python con FastAPI
*   **Base de Datos:** PostgreSQL en Supabase (desde el día 1)
*   **ORM y Migraciones:** SQLAlchemy 2 + Alembic
*   **Frontend:** Vue 3 (Composition API) + Vite + Tailwind CSS 4

## 3. Estado Actual
*   [Completado] Estructura base del backend y del frontend.
*   [Pendiente] Agregar DATABASE_URL de Supabase en backend/.env.
*   [Pendiente] Inicializar repositorio Git.

## 4. Estructura del Proyecto

### backend/
*   `app/main.py`: arranque de FastAPI y CORS.
*   `app/core/config.py`: variables de entorno.
*   `app/core/database.py`: motor SQLAlchemy, Base y sesión.
*   `app/routers/`: rutas de la API.
*   `app/models/`: modelos de base de datos.
*   `app/schemas/`: esquemas Pydantic.
*   `alembic/`: migraciones.
*   `.env`: variables locales (no se sube a Git).

### frontend/
*   `src/App.vue`: pantalla de bienvenida mobile-first.
*   `src/style.css`: import de Tailwind.
*   `vite.config.js`: plugins de Vue y Tailwind, proxy `/api`.

## 5. Comandos Útiles

### Backend
*   Iniciar: `cd backend && .venv/bin/uvicorn app.main:app --reload`
*   Migración: `cd backend && .venv/bin/alembic revision --autogenerate -m "mensaje"`
*   Aplicar: `cd backend && .venv/bin/alembic upgrade head`

### Frontend
*   Iniciar: `cd frontend && npm run dev`

## 6. Fases de Desarrollo (Roadmap)

### Fase 1: Base y MVP (Público)
- [x] Configurar servidor FastAPI base (Carpeta: backend).
- [x] Inicializar proyecto Vue 3 + Vite + Tailwind (Carpeta: frontend).
- [ ] Crear interfaz Mobile-First de bienvenida.
- [ ] Conectar Supabase y crear la primera migración.

### Fase 2: Gestión Interna e Inventario
- [ ] Sistema de Autenticación.
- [ ] Módulo de Inventario de Plántulas.
- [ ] Módulo de Tiempos de Riego y Cosecha.

### Fase 3: Módulos Especializados
- [ ] Módulo de Meliponicultura (Abejas sin aguijón).
- [ ] Módulo de Lombricultura.

## 7. Registro de Cambios
*   2026-09-30: Estructura base creada. Backend con FastAPI, SQLAlchemy y Alembic. Frontend con Vue 3, Vite y Tailwind 4. Ambos probados.
