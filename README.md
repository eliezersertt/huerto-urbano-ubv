# Huerto Urbano

Aplicacion web Mobile-First para la gestion de un huerto universitario.

## Estructura

- backend: API con FastAPI, SQLAlchemy y Alembic.
- frontend: Vue 3 con Vite y Tailwind CSS 4.

## Backend

1. Crear el entorno virtual.

   python3 -m venv backend/.venv

2. Instalar dependencias.

   backend/.venv/bin/pip install -r backend/requirements.txt

3. Copiar backend/.env.example a backend/.env.
   Usa el pooler de Supabase, no la conexion directa.
   Formato: postgresql+psycopg://postgres.<ref>@aws-0-us-east-2.pooler.supabase.com:5432/postgres
   La conexion directa es solo IPv6 y puede fallar.

4. Iniciar el servidor.

   cd backend
   .venv/bin/uvicorn app.main:app --reload

La documentacion queda en http://127.0.0.1:8000/docs

## Migraciones

   cd backend
   .venv/bin/alembic revision --autogenerate -m "descripcion"
   .venv/bin/alembic upgrade head

## Frontend

1. Instalar dependencias.

   cd frontend
   npm install

2. Iniciar el servidor.

   npm run dev

La app queda en http://localhost:5173
