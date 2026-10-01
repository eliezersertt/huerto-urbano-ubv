# Guía de demostración — Huerto Urbano (UBV)

## Antes de empezar

1. Coloca el logo oficial en la carpeta.
   Ruta: frontend/public/logo-ubv.png
   Es opcional. Sin él se verá un texto "UBV".

2. Abre dos terminales.

3. Terminal 1 (backend).
   cd backend
   .venv/bin/uvicorn app.main:app --reload

4. Terminal 2 (frontend).
   cd frontend
   npm run dev

5. Abre en el navegador:
   http://localhost:5173

## Recorrido sugerido

### 1. Portada principal
- Qué mostrar: el lema "La Casa de los Saberes".
- El logo en el círculo blanco.
- El botón verde "Explorar el Censo Arbóreo".
- Qué decir: "Es un huerto universitario de la UBV
  para la agroecología y el desarrollo sustentable."

### 2. Censo arbóreo
- Clic en el botón verde o en "Censo Arbóreo".
- Mostrar la lista de 145 ejemplares.
- Señalar el número de placa en cada árbol.
- Qué decir: "Cada árbol tiene una placa física.
  Aquí se ve su registro digital."

### 3. Ficha con QR
- Tocar un árbol de la lista.
- Se abre la ficha con sus datos.
- Mostrar el código QR.
- Qué decir: "Escaneando este QR se abre la ficha
  desde la placa real del árbol."

### 4. Secciones futuras
- Usar el menú de arriba para mostrar:
  Inventario, Ciclos y Horarios, Semilleros, Responsables.
- Qué decir: "Estas son maquetas visuales.
  Aún no son funcionales."

## Puntos fuertes para destacar

1. Identidad institucional UBV (azul marino).
2. Diseño Mobile-First. Se ve bien en el teléfono.
3. El QR conecta lo digital con las placas físicas.
4. Datos reales del censo de la parcela sur.
5. Base de datos en la nube (Supabase).

## Preguntas posibles

### ¿Ya está en producción?
No. Es una base en desarrollo.

### ¿Dónde están los datos?
En Supabase, una base de datos PostgreSQL en la nube.

### ¿Qué sigue?
Autenticación, inventario real y tiempos de riego.

## Nota final

No necesitas internet para la demo local.
Todo corre en tu computadora.
El backend usa la nube solo para leer los datos del censo.
