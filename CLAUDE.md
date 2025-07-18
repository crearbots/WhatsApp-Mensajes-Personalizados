# CLAUDE.md

Este archivo proporciona guía a Claude Code (claude.ai/code) cuando trabaja con código en este repositorio.

## Comandos Comunes

### Configuración del Entorno
```bash
# Activar entorno virtual
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar script de configuración (Linux/Mac)
./setup.sh

# Ejecutar la aplicación principal
python gui.py
```

### Desarrollo
```bash
# Ejecutar la aplicación con interfaz gráfica
python gui.py

# Ejecutar solo el motor de mensajes (sin GUI)
python app.py
```

## Arquitectura del Proyecto

### Componentes Principales
- **gui.py**: Interfaz gráfica principal usando Tkinter - punto de entrada del usuario
- **app.py**: Motor de automatización de WhatsApp - maneja el envío de mensajes
- **mensaje.py**: Ventana modal para composición de mensajes con validación
- **Contactos.xlsx**: Archivo Excel con datos de contactos (Nombre, Celular, Genero)

### Patrón de Arquitectura
El proyecto sigue un patrón de **separación de responsabilidades**:
- **Presentación**: `gui.py` maneja toda la interfaz de usuario
- **Lógica de Negocio**: `app.py` contiene la lógica de automatización
- **Utilidades**: `mensaje.py` proporciona funcionalidades auxiliares

### Flujo de Datos
1. Usuario configura parámetros en `gui.py`
2. `mensaje.py` captura y valida el mensaje personalizado
3. `app.py` lee `Contactos.xlsx` y ejecuta automatización con PyAutoGUI
4. Cada contacto recibe mensaje personalizado vía WhatsApp Web

## Optimizaciones para Migración Web

### Separación de Capas Recomendada

#### Backend (Python/Flask o FastAPI)
```
/backend
├── api/
│   ├── routes/
│   │   ├── contacts.py      # CRUD de contactos
│   │   ├── messages.py      # Composición de mensajes
│   │   └── campaigns.py     # Gestión de campañas
│   ├── services/
│   │   ├── whatsapp_service.py  # Lógica de WhatsApp
│   │   ├── contact_service.py   # Lógica de contactos
│   │   └── message_service.py   # Procesamiento de mensajes
│   ├── models/
│   │   ├── contact.py
│   │   ├── message.py
│   │   └── campaign.py
│   └── utils/
│       ├── validators.py
│       └── formatters.py
├── database/
│   └── models.py
└── config/
    └── settings.py
```

#### Frontend (React)
```
/frontend
├── src/
│   ├── components/
│   │   ├── ContactManager/
│   │   ├── MessageComposer/
│   │   ├── CampaignDashboard/
│   │   └── FileUploader/
│   ├── services/
│   │   ├── api.js
│   │   ├── contactService.js
│   │   └── messageService.js
│   ├── hooks/
│   │   ├── useContacts.js
│   │   └── useMessages.js
│   └── utils/
│       ├── validators.js
│       └── formatters.js
```

### Módulos Listos para Migración

#### 1. **Módulo de Contactos** (Basado en lógica actual de Excel)
- **Función actual**: Lectura de `Contactos.xlsx`
- **Migración**: API REST para CRUD de contactos
- **Estructura**: `GET /api/contacts`, `POST /api/contacts`, etc.

#### 2. **Módulo de Mensajes** (Basado en `mensaje.py`)
- **Función actual**: Validación y codificación de mensajes
- **Migración**: Servicio de composición con plantillas
- **Mejoras**: Editor WYSIWYG, vista previa en tiempo real

#### 3. **Módulo de Campañas** (Basado en `app.py`)
- **Función actual**: Envío secuencial con tiempos de espera
- **Migración**: Cola de trabajos asíncronos (Celery/Redis)
- **Mejoras**: Programación, reintentos, estadísticas

#### 4. **Módulo de Automatización**
- **Función actual**: PyAutoGUI para interactuar con WhatsApp Web
- **Migración**: API de WhatsApp Business o bibliotecas como `whatsapp-web.js`
- **Ventajas**: Más estable, sin dependencia de GUI

### Dependencias Actuales vs Web

#### Actuales (Desktop)
```
PyAutoGUI==0.9.54  # Automatización GUI
openpyxl==3.1.5    # Lectura Excel
pandas==2.2.3      # Manipulación datos
tkinter             # GUI desktop
```

#### Propuestas (Web)
```python
# Backend
fastapi==0.104.1    # API REST
sqlalchemy==2.0.23  # ORM database
celery==5.3.4       # Cola de trabajos
redis==5.0.1        # Cache/cola
pandas==2.2.3       # Mantener para procesamiento
```

```javascript
// Frontend
react==18.2.0
axios==1.6.0        # HTTP client
react-query==3.39.3 # Estado servidor
material-ui         # Componentes UI
```

### Puntos de Migración Críticos

1. **Reemplazar PyAutoGUI**: Usar WhatsApp Business API o bibliotecas web
2. **Migrar Tkinter**: Convertir a componentes React reutilizables
3. **Centralizar Configuración**: Mover parámetros hardcodeados a base de datos
4. **Asegurar Escalabilidad**: Implementar cola de trabajos para múltiples usuarios

### Configuración Actual de Tiempos
```python
# Valores por defecto optimizados encontrados en gui.py
TIEMPO_CARGA = 15      # Carga WhatsApp Web
TIEMPO_CLICK = 3       # Entre click y escritura
TIEMPO_ENVIO = 3       # Entre envío de mensajes
TIEMPO_CERRAR = 3      # Antes de cerrar pestaña
COORDENADAS = (900, 450)  # Click en caja de texto
```

Estos valores deben convertirse en configuraciones dinámicas en la versión web.