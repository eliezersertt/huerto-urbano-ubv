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
*   [Completado] Modelo Plant en inglés y migrado a Supabase.
*   [Completado] Esquemas Pydantic y router de plants (listar, ver, crear).
*   [Completado] Base poblada con 145 filas desde plantas.md.
*   [Completado] Campos de censo: census_number, dap y trunk_shape.
*   [Completado] Textos limpiados: nombres en Título y científicos capitalizados.
*   [Completado] Frontend: listado y ficha de planta con router.
*   [Completado] Generación de QR en SVG apuntando a /planta/{census}.

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
*   `app/schemas/plant.py`: esquemas Pydantic de Plant.
*   `app/routers/plants.py`: rutas listar, ver y crear.
*   `app/schemas/`: esquemas Pydantic.
*   `alembic/`: migraciones.
*   `scripts/seed_plants.py`: poblar la base desde plantas.md.
*   `.env`: variables locales (no se sube a Git).

### Tabla plants
Campos del modelo Plant, todos en inglés.
*   `id`: entero, clave primaria.
*   `census_number`: entero, único. Es el número de la placa física.
*   `common_name`: texto, opcional, máximo 120.
*   `scientific_name`: texto, opcional, máximo 160.
*   `origin`: texto, opcional, máximo 120.
*   `dap`: número decimal (cm), opcional.
*   `trunk_shape`: texto, opcional, máximo 80.
*   `height`: número decimal (metros), opcional.
*   `qr_code_url`: texto, opcional, máximo 500, con índice.

### frontend/
*   `src/App.vue`: shell con navbar y RouterView.
*   `src/components/AppNavbar.vue`: menú de navegación superior.
*   `src/router/index.js`: rutas de todas las secciones.
*   `src/views/HomeView.vue`: portada principal (landing) en `/`.
*   `src/views/PlantListView.vue`: censo arbóreo en `/censo`.
*   `src/views/PlantDetailView.vue`: ficha de planta con QR.
*   `src/views/InventoryView.vue`: maqueta de Inventario.
*   `src/views/CyclesView.vue`: maqueta de Ciclos y Horarios.
*   `src/views/SeedbedsView.vue`: maqueta de Semilleros.
*   `src/views/PeopleView.vue`: maqueta de Responsables.
*   `src/style.css`: tokens de color, tipografía y sombras.
*   `vite.config.js`: plugins de Vue y Tailwind, proxy `/api`.

## 4.1 Identidad Visual UBV
*   Color principal: azul marino UBV (#14306b). Estructura y textos fuertes.
*   Verde (#2e7d4f): solo acento. Botones, hojas e íconos.
*   Tipografía: Fraunces (títulos) y Public Sans (texto).
*   Logo oficial: colocar en `frontend/public/logo-ubv.png`.
    La portada muestra un espacio circular reservado para él.

## 5. Comandos Útiles

### Backend
*   Iniciar: `cd backend && .venv/bin/uvicorn app.main:app --reload`
*   Migración: `cd backend && .venv/bin/alembic revision --autogenerate -m "mensaje"`
*   Aplicar: `cd backend && .venv/bin/alembic upgrade head`
*   Poblar: `cd backend && .venv/bin/python scripts/seed_plants.py`

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
*   2026-09-30: Columnas de plants renombradas a inglés. Migración 27af2fbbf3b9. Esquemas, router y script seed_plants.py creados. 145 filas importadas desde plantas.md.
*   2026-09-30: Añadidos census_number, dap y trunk_shape. Migración 538ce093b0cb. Textos limpiados. QR en SVG. Frontend con listado y ficha de planta.
*   2026-10-01: Skill frontend-design instalada. Rediseño orgánico del frontend. Navbar y 4 maquetas visuales: Inventario, Ciclos y Horarios, Semilleros y Responsables.
*   2026-10-01: Pivote a identidad UBV. Azul marino principal, verde de acento. Portada en `/`, censo movido a `/censo`. Logo reservado en `/logo-ubv.png`.
