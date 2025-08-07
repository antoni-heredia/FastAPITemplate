# FastAPI Template

Plantilla mínima para trabajar con FastAPI y ClickHouse en un entorno local.

## Requisitos
- Docker y Docker Compose

## Uso
1. Construir e iniciar los contenedores:
   ```bash
   docker compose up --build
   ```
2. Abrir [http://localhost:8000/ping](http://localhost:8000/ping) para verificar la conexión con ClickHouse.
3. Insertar y consultar usuarios de ejemplo:
   - `POST /users` con cuerpo JSON `{ "id": 1, "name": "Alice", "age": 30 }`
   - `GET /users` devuelve la lista de usuarios registrados
