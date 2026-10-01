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

2. Crear el archivo de entorno.

   Copia frontend/.env.example a frontend/.env
   Ajusta VITE_API_URL si tu backend usa otro puerto.

3. Iniciar el servidor.

   npm run dev

La app queda en http://localhost:5173

## Despliegue en la nube

### Backend en Render

1. Crea un Web Service apuntando a la carpeta backend.
2. Comando de arranque:

   uvicorn app.main:app --host 0.0.0.0 --port $PORT

3. Variables de entorno en Render:

   DATABASE_URL=postgresql+psycopg://postgres.<ref>@aws-0-us-east-2.pooler.supabase.com:5432/postgres
   CORS_ORIGINS=["*"]
   PUBLIC_BASE_URL=https://tu-app.vercel.app
   PYTHON_VERSION=3.13.5

4. Tras el primer despliegue, aplica las migraciones una vez.

   alembic upgrade head

### Frontend en Vercel

1. Importa el repositorio y elige la carpeta frontend.
2. Comando de build: npm run build
3. Carpeta de salida: dist
4. Variable de entorno en Vercel:

   VITE_API_URL=https://tu-backend.onrender.com

### Orden recomendado

1. Despliega primero el backend en Render.
2. Copia su URL y ponla en VITE_API_URL en Vercel.
3. Copia la URL de Vercel y ponla en PUBLIC_BASE_URL en Render.
4. Vuelve a desplegar para que los QR apunten al dominio real.

## Nota sobre CORS

Ahora mismo el backend acepta cualquier origen (CORS_ORIGINS=["*"]).

Es temporal, para facilitar las pruebas.

Cuando el dominio este fijo, cambialo por la URL de Vercel.

