# Clase 1 - Configuración de Repositorio y Primer Desafío

## Aplicación Elegida: Apache HTTP Server (httpd)

### Comandos Ejecutados

#### 1. Despliegue del Container
```bash
docker run -d --name mi-apache -p 8081:80 httpd
```

**Explicación de los flags:**
- `-d`: Ejecuta el container en modo "detached" (segundo plano)
- `--name mi-apache`: Asigna el nombre "mi-apache" al container para identificarlo fácilmente
- `-p 8081:80`: Mapea el puerto 8081 de mi máquina host al puerto 80 del container
- `httpd`: Nombre de la imagen Docker a utilizar (Apache HTTP Server)

#### 2. Verificación del Container
```bash
# Listar containers en ejecución
docker ps

# Consultar logs del container
docker logs mi-apache

# Acceder desde el navegador: http://localhost:8081
```

#### 3. Limpieza
```bash
# Detener el container
docker stop mi-apache

# Eliminar el container
docker rm mi-apache

# Verificar eliminación
docker ps -a | grep mi-apache
```

### Evidencias

#### Container en Ejecución
![Docker PS](./screenshots/docker-ps.png)

#### Apache Funcionando
![Apache en Navegador](./screenshots/apache-running.png)

#### Container Eliminado
![Container Eliminado](./screenshots/container-removed.png)

### Conclusiones

**Aprendizajes:**
- Comprensión del ciclo de vida de un container Docker
- Uso de flags básicos de `docker run`
- Mapeo de puertos entre host y container
- Comandos de gestión de containers

**Dificultades encontradas:**
- [Describe aquí cualquier problema que hayas tenido y cómo lo resolviste]

---

*Fecha de realización: [Fecha Actual]*
