# EC2 Manager API

API REST para gestión simulada de instancias EC2 usando FastAPI y boto3.

## Descripción

Esta API simula operaciones básicas de gestión de instancias EC2 para equipos DBA que automatizan la gestión de infraestructura. Utiliza datos mock para simular respuestas de AWS EC2 sin necesidad de acceso real a la nube.

## Características

- ✅ **GET /instances** - Lista todas las instancias EC2 simuladas
- ✅ **POST /instances/{id}/stop** - Simula detener una instancia específica
- ✅ **GET /instances/{id}** - Obtiene información de una instancia específica
- ✅ Uso de **tipos específicos** para estados y tipos de instancias EC2
- ✅ **Manejo de errores** robusto con códigos HTTP apropiados
- ✅ **Logging** detallado para debugging y monitoreo
- ✅ **Documentación automática** con Swagger/OpenAPI
- ✅ **Tests unitarios** y de integración completos
- ✅ **Mocks** usando moto para simular boto3

## Tecnologías Utilizadas

- **FastAPI**: Framework web moderno y rápido
- **Pydantic**: Validación de datos y serialización
- **boto3**: SDK de AWS para Python
- **moto**: Librería para mockear servicios AWS
- **pytest**: Framework de testing
- **uvicorn**: Servidor ASGI

## Instalación y Configuración

### Prerrequisitos

- Python 3.8+
- pip o poetry

### Pasos de instalación

1. **Clonar el repositorio**:
   ```bash
   git clone <repository-url>
   cd ec2-manager-api
   ```

2. **Crear entorno virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

### Desarrollo

```bash
# Ejecutar el servidor de desarrollo
python -m src.app

# O usando uvicorn directamente
uvicorn src.app:app --reload --host 0.0.0.0 --port 8000
```

### Producción

```bash
uvicorn src.app:app --host 0.0.0.0 --port 8000
```

La API estará disponible en: `http://localhost:8000`

## Documentación de la API

Una vez que el servidor esté ejecutándose, puedes acceder a:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
- **OpenAPI JSON**: `http://localhost:8000/openapi.json`

## Endpoints

### GET /instances

Retorna una lista de todas las instancias EC2 simuladas.

**Respuesta exitosa (200)**:
```json
[
  {
    "id": "i-1234567890abcdef0",
    "name": "web-server-prod",
    "type": "t3.medium",
    "state": "running",
    "region": "us-east-1",
    "launch_time": "2024-01-15T10:30:00Z",
    "private_ip": "10.0.1.10",
    "public_ip": "54.123.45.67"
  }
]
```

### GET /instances/{id}

Obtiene información de una instancia específica.

**Parámetros**:
- `id` (string): ID de la instancia

**Respuestas**:
- **200**: Instancia encontrada
- **404**: Instancia no encontrada

### POST /instances/{id}/stop

Simula detener una instancia EC2.

**Parámetros**:
- `id` (string): ID de la instancia a detener

**Respuesta exitosa (200)**:
```json
{
  "success": true,
  "message": "Instance i-1234567890abcdef0 is now stopping",
  "instance_id": "i-1234567890abcdef0",
  "previous_state": "running",
  "current_state": "stopping"
}
```

**Respuestas de error**:
- **400**: No se puede detener la instancia (estado inválido)
- **404**: Instancia no encontrada
- **500**: Error interno del servidor

## Tipos de Datos

### Estados de Instancia (InstanceState)

- `pending`: Instancia iniciándose
- `running`: Instancia en ejecución
- `shutting-down`: Instancia apagándose
- `terminated`: Instancia terminada
- `stopping`: Instancia deteniéndose
- `stopped`: Instancia detenida

### Tipos de Instancia (InstanceType)

- `t2.micro`, `t2.small`, `t2.medium`
- `t3.micro`, `t3.small`, `t3.medium`
- `m5.large`, `m5.xlarge`
- `c5.large`, `c5.xlarge`

### Regiones AWS (AWSRegion)

- `us-east-1`, `us-west-1`, `us-west-2`
- `eu-west-1`, `eu-central-1`
- `ap-southeast-1`, `ap-northeast-1`
- `sa-east-1`

## Testing

### Ejecutar todos los tests

```bash
pytest
```

### Ejecutar tests con coverage

```bash
pytest --cov=src --cov-report=html
```

### Ejecutar tests específicos

```bash
# Tests del servicio EC2
pytest tests/test_ec2_service.py

# Tests de las rutas
pytest tests/test_instances.py

# Tests por categoría
pytest -m unit
pytest -m integration
```

### Estructura de Tests

- `tests/test_ec2_service.py`: Tests unitarios del servicio EC2
- `tests/test_instances.py`: Tests de integración de las rutas API

## Datos Mock

La API utiliza datos simulados que incluyen 5 instancias de ejemplo con diferentes estados:

1. **web-server-prod** (running) - t3.medium en us-east-1
2. **database-server** (running) - m5.large en us-east-1
3. **test-environment** (stopped) - t2.micro en us-west-2
4. **monitoring-server** (running) - t3.small en eu-west-1
5. **backup-server** (stopping) - c5.large en ap-southeast-1

## Estructura del Proyecto

```
ec2-manager-api/
├── src/
│   ├── __init__.py
│   ├── app.py                 # Aplicación FastAPI principal
│   ├── models/
│   │   ├── __init__.py
│   │   └── instance.py        # Modelos Pydantic con tipos
│   ├── routes/
│   │   ├── __init__.py
│   │   └── instances.py       # Rutas de la API
│   ├── services/
│   │   ├── __init__.py
│   │   └── ec2_service.py     # Lógica de negocio EC2
│   └── utils/
│       ├── __init__.py
│       └── mock_data.py       # Datos simulados
├── tests/
│   ├── __init__.py
│   ├── test_ec2_service.py    # Tests del servicio
│   └── test_instances.py      # Tests de rutas
├── pytest.ini                # Configuración de pytest
├── requirements.txt           # Dependencias
└── README.md                 # Este archivo
```

## Características Técnicas

### Manejo de Errores

- Validación automática de parámetros con Pydantic
- Códigos de estado HTTP apropiados
- Mensajes de error descriptivos
- Logging de errores para debugging

### Logging

- Configuración centralizada de logging
- Logs estructurados con timestamps
- Diferentes niveles de log (INFO, WARNING, ERROR)
- Logs de operaciones críticas

### Validación de Datos

- Tipos estrictos con enums para estados y tipos
- Validación automática de entrada
- Respuestas tipadas con Pydantic

### Simulación Realista

- Estados de transición de instancias
- Validación de operaciones según estado actual
- Datos mock realistas con IPs y metadatos

## Mejoras Futuras

- [ ] Autenticación y autorización
- [ ] Rate limiting
- [ ] Métricas y monitoreo
- [ ] Base de datos persistente
- [ ] Más operaciones EC2 (start, restart, terminate)
- [ ] Webhooks para notificaciones
- [ ] Filtros y paginación en listado
- [ ] Cache con Redis
- [ ] Containerización con Docker

## Contribución

1. Fork del proyecto
2. Crear rama feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit de cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crear Pull Request

## Licencia

MIT License - ver archivo LICENSE para detalles.

## Contacto

DBA Team - dba-team@company.com

---

**Nota**: Esta es una simulación para propósitos educativos y de testing. No realiza operaciones reales en AWS.
