# Etapa 1: Build
FROM python:3.11-slim AS builder

WORKDIR /app

# Copiar archivo de dependencias
COPY requirements.txt .

# Instalar dependencias en directorio de usuario
RUN pip install --user --no-cache-dir -r requirements.txt

# Etapa 2: Production
FROM python:3.11-slim

WORKDIR /app

# Crear usuario no-root
RUN useradd -m -u 1001 appuser

# Copiar dependencias desde la etapa de build
COPY --from=builder /root/.local /home/appuser/.local

# Copiar código de la aplicación
COPY --chown=appuser:appuser app.py .

# Cambiar al usuario no-root
USER appuser

# Configurar PATH para usar las dependencias instaladas
ENV PATH=/home/appuser/.local/bin:$PATH

# Exponer el puerto
EXPOSE 5000

# Variable de entorno por defecto
ENV PORT=5000

# Comando de inicio
CMD ["python", "app.py"]
