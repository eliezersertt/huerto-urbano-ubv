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
*   [Completado] Repositorio Git inicializado con el primer commit.
*   [Completado] Conexión a Supabase verificada. Migración base aplicada.
*   [Completado] DATABASE_URL configurada en backend/.env.
*   [Completado] Modelo Plant creado y migrado a Supabase.

## 3.1 Conexión a Supabase (IMPORTANTE)
*   La conexión directa (db.<ref>.supabase.co) es solo IPv6 y falla aquí.
*   Se usa el pooler de IPv4. Host: aws-0-us-east-2.pooler.supabase.com
*   Puerto: 5432 (modo sesión, obligatorio para Alembic).
*   Usuario del pooler: postgres.<ref-del-proyecto>
*   La clave contiene el símbolo de porcentaje. Por eso Alembic lee la URL
    desde app/core/config.py y no desde el archivo alembic.ini.

## 4. Estructura del Proyecto

### backend/
*   `app/main.py`: arranque de FastAPI y CORS.
*   `app/core/config.py`: variables de entorno.
*   `app/core/database.py`: motor SQLAlchemy, Base y sesión.
*   `app/routers/`: rutas de la API.
*   `app/models/`: modelos de base de datos.
*   `app/models/plant.py`: modelo Plant (tabla `plants`).
*   `app/schemas/`: esquemas Pydantic.
*   `alembic/`: migraciones.
*   `.env`: variables locales (no se sube a Git).

### Tabla plants
Campos del modelo Plant para lectura de códigos QR.
*   `id`: entero, clave primaria.
*   `nombre_comun`: texto, obligatorio, máximo 120.
*   `especie_cientifica`: texto, opcional, máximo 160.
*   `descripcion`: texto largo, opcional.
*   `qr_code_url`: texto, opcional, máximo 500, con índice.

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
- [x] Crear interfaz Mobile-First de bienvenida.
- [x] Conectar Supabase y crear la primera migración.

### Fase 2: Gestión Interna e Inventario
- [ ] Sistema de Autenticación.
- [ ] Módulo de Inventario de Plántulas.
- [ ] Módulo de Tiempos de Riego y Cosecha.

### Fase 3: Módulos Especializados
- [ ] Módulo de Meliponicultura (Abejas sin aguijón).
- [ ] Módulo de Lombricultura.

## 7. Registro de Cambios
*   2026-09-30: Estructura base creada. Backend con FastAPI, SQLAlchemy y Alembic. Frontend con Vue 3, Vite y Tailwind 4. Ambos probados.
*   2026-09-30: Repositorio Git inicializado. Commit inicial fa69ac3.
*   2026-09-30: Conexión a Supabase vía pooler IPv4. Migración 8045eee03791 aplicada. Endpoint /health responde con database ok.
*   2026-09-30: Modelo Plant creado. Migración a5111ffa4082 aplicada. Tabla plants creada en Supabase con 5 columnas.
