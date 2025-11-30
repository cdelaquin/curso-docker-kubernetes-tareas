# Mi Aplicación Dockerizada

## Descripción
Aplicación Node.js/Express dockerizada con multi-stage build

## Endpoints
- `GET /` - Mensaje de bienvenida
- `GET /health` - Estado de salud de la aplicación

## Uso Local
```bash
docker pull tu-usuario/mi-app-node:latest
docker run -p 3000:3000 tu-usuario/mi-app-node:latest
```

## Construcción
```bash
docker build -t mi-app-node:1.0 .
```

## Variables de Entorno
- `PORT` - Puerto de la aplicación (default: 3000)
