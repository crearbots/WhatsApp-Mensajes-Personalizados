# 📱 WhatsApp Mensajes Personalizados

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-GPL3.0-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)](https://github.com/usuario/WhatsApp-Mensajes-Personalizados)

> **Herramienta de automatización para envío masivo de mensajes personalizados en WhatsApp**

Una aplicación de escritorio desarrollada en Python que permite automatizar el envío de mensajes personalizados a múltiples contactos de WhatsApp, con soporte para variables dinámicas, archivos multimedia y configuración flexible de tiempos de envío.

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Descripción del Programa](#-descripción-del-programa)
- [Instalación Rápida](#-instalación-rápida)
- [Guía de Uso](#-guía-de-uso)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Migración Web](#-migración-web)
- [Tutoriales de Automatización](#-tutoriales-de-automatización)
- [Solución de Problemas](#-solución-de-problemas)
- [Contribuciones](#-contribuciones)
- [Licencia](#-licencia)

## ✨ Características

- **🎯 Mensajes Personalizados**: Utiliza variables como `{nombre}` y `{genero}` para personalizar cada mensaje
- **📊 Gestión de Contactos**: Importa contactos desde archivos Excel (.xlsx)
- **🖼️ Archivos Multimedia**: Envía imágenes, videos y documentos adjuntos
- **⏰ Control de Tiempos**: Configuración flexible de tiempos de espera y envío
- **🖥️ Interfaz Gráfica**: GUI intuitiva desarrollada con Tkinter
- **🛠️ Configuración Avanzada**: Personalización de coordenadas y parámetros de automatización
- **📦 Instalación Automatizada**: Scripts de configuración para Windows y Linux/macOS

## 🔍 Descripción del Programa

### ¿Qué hace?
Este programa automatiza el envío masivo de mensajes personalizados en WhatsApp Web, permitiendo a los usuarios:
- Enviar mensajes a múltiples contactos con contenido personalizado
- Incluir variables dinámicas que se reemplazan automáticamente
- Adjuntar archivos multimedia (imágenes, videos)
- Configurar tiempos de espera personalizados para evitar bloqueos

### Arquitectura del Sistema
El proyecto está estructurado con separación de responsabilidades:

```
WhatsApp-Mensajes-Personalizados/
├── gui.py          # Interfaz gráfica principal
├── app.py          # Motor de automatización
├── mensaje.py      # Gestión de mensajes
├── Contactos.xlsx  # Base de datos de contactos
├── setup.sh        # Instalación para Linux/macOS
├── setup.bat       # Instalación para Windows
└── requirements.txt # Dependencias Python
```

### Tecnologías Utilizadas
- **Python 3.8+**: Lenguaje principal
- **Tkinter**: Interfaz gráfica de usuario
- **PyAutoGUI**: Automatización de interfaz
- **Pandas**: Procesamiento de datos Excel
- **OpenPyXL**: Manipulación de archivos Excel

## 🚀 Instalación Rápida

### Requisitos del Sistema
- Python 3.8 o superior
- Google Chrome (para WhatsApp Web)
- Acceso a internet
- Permisos de administrador (para instalación de dependencias)

### Instalación Automática

#### Windows
```bash
# Descargar el proyecto y ejecutar
setup.bat
```

#### Linux/macOS
```bash
# Hacer ejecutable y ejecutar
chmod +x setup.sh
./setup.sh
```

### Ejecución Rápida

Una vez instalado, puedes ejecutar la aplicación usando los scripts generados:

#### Windows
```bash
run.bat
```

#### Linux/macOS
```bash
./run.sh
```

## 📖 Guía de Uso

### 1. Preparación del Archivo de Contactos

Crea o edita el archivo `Contactos.xlsx` con la siguiente estructura:

| Nombre | Celular | Genero |
|--------|---------|--------|
| Juan   | +1234567890 | Sr. |
| María  | +0987654321 | Sra. |

**Importante**: El número debe incluir el código de país (ej: +52 para México).

### 2. Configuración de WhatsApp Web

1. Abre Google Chrome
2. Ve a [web.whatsapp.com](https://web.whatsapp.com)
3. Escanea el código QR con tu teléfono
4. Mantén la sesión activa

### 3. Uso de la Aplicación

1. **Ejecutar la aplicación**:
   ```bash
   python gui.py
   ```

2. **Seleccionar archivo de contactos**: Haz clic en "Seleccionar archivo" y elige tu archivo Excel

3. **Escribir mensaje**: Haz clic en "Escribir Mensaje" y usa variables como:
   ```
   Hola {genero} {nombre}, espero que tengas un excelente día.
   ```

4. **Configurar parámetros**:
   - Tiempo de carga: 15 segundos (recomendado)
   - Tiempo entre clicks: 3 segundos
   - Coordenadas: Ajustar según tu pantalla

5. **Iniciar envío**: Haz clic en "Iniciar envío de mensajes"

### 4. Envío de Archivos Multimedia

1. Haz clic en "Seleccionar imagen o video"
2. Elige el archivo que deseas enviar
3. El archivo se enviará automáticamente con cada mensaje

## 🏗️ Estructura del Proyecto

```
WhatsApp-Mensajes-Personalizados/
├── 📁 venv/                    # Entorno virtual
├── 📄 gui.py                   # Interfaz gráfica principal
├── 📄 app.py                   # Motor de automatización
├── 📄 mensaje.py               # Gestión de mensajes
├── 📄 Contactos.xlsx           # Base de datos de contactos
├── 📄 requirements.txt         # Dependencias Python
├── 📄 setup.sh                 # Script de instalación Linux/macOS
├── 📄 setup.bat                # Script de instalación Windows
├── 📄 run.sh                   # Script de ejecución Linux/macOS
├── 📄 run.bat                  # Script de ejecución Windows
├── 📄 CLAUDE.md                # Documentación técnica
├── 📄 README.md                # Este archivo
└── 📄 LICENSE                  # Licencia MIT
```

## 🌐 Migración Web

Esta sección proporciona guías completas para migrar la aplicación a una arquitectura web moderna, con dos enfoques diferentes según las necesidades del proyecto.

### 📊 Comparativa de Enfoques

| Aspecto | whatsapp-web.js + Node.js | PyAutoGUI + Python Web |
|---------|---------------------------|-------------------------|
| **Facilidad de Implementación** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Escalabilidad** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Estabilidad** | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Mantenimiento** | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Curva de Aprendizaje** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Reutilización de Código** | ⭐⭐ | ⭐⭐⭐⭐⭐ |

### 🎯 Recomendaciones

- **Para proyectos nuevos**: whatsapp-web.js + Node.js
- **Para migración rápida**: PyAutoGUI + Python Web
- **Para alta escalabilidad**: whatsapp-web.js + Node.js
- **Para prototipado rápido**: PyAutoGUI + Python Web

## 🔧 Tutoriales de Automatización

### 🟢 Opción 1: whatsapp-web.js + Node.js (Recomendado)

**Ventajas**:
- ✅ Mayor estabilidad y confiabilidad
- ✅ No depende de la interfaz gráfica
- ✅ Mejor escalabilidad para múltiples usuarios
- ✅ API más robusta y mantenible
- ✅ Soporte para funcionalidades avanzadas

**Desventajas**:
- ❌ Requiere reescribir toda la lógica
- ❌ Curva de aprendizaje de Node.js
- ❌ Mayor complejidad inicial

#### Instalación y Configuración

```bash
# Crear nuevo proyecto Node.js
mkdir whatsapp-automation-node
cd whatsapp-automation-node
npm init -y

# Instalar dependencias
npm install whatsapp-web.js qrcode-terminal xlsx express multer
```

#### Ejemplo de Implementación

```javascript
// server.js
const { Client, LocalAuth } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');
const XLSX = require('xlsx');
const express = require('express');
const multer = require('multer');

const app = express();
const upload = multer({ dest: 'uploads/' });

// Configurar cliente WhatsApp
const client = new Client({
    authStrategy: new LocalAuth(),
    puppeteer: {
        headless: false,
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    }
});

// Generar QR Code
client.on('qr', (qr) => {
    console.log('Escanea el código QR:');
    qrcode.generate(qr, { small: true });
});

// Cliente listo
client.on('ready', () => {
    console.log('Cliente WhatsApp conectado!');
});

// Función para enviar mensajes personalizados
async function enviarMensajesPersonalizados(archivo, mensaje, imagenPath = null) {
    try {
        // Leer archivo Excel
        const workbook = XLSX.readFile(archivo);
        const sheetName = workbook.SheetNames[0];
        const worksheet = workbook.Sheets[sheetName];
        const contactos = XLSX.utils.sheet_to_json(worksheet);

        for (const contacto of contactos) {
            const { Nombre, Celular, Genero } = contacto;
            
            // Personalizar mensaje
            const mensajePersonalizado = mensaje
                .replace('{nombre}', Nombre)
                .replace('{genero}', Genero);

            // Formatear número
            const numeroFormateado = Celular.replace(/\D/g, '');
            const chatId = `${numeroFormateado}@c.us`;

            try {
                // Enviar mensaje
                await client.sendMessage(chatId, mensajePersonalizado);
                
                // Enviar imagen si existe
                if (imagenPath) {
                    const media = MessageMedia.fromFilePath(imagenPath);
                    await client.sendMessage(chatId, media);
                }

                console.log(`Mensaje enviado a ${Nombre} (${Celular})`);
                
                // Esperar entre envíos
                await new Promise(resolve => setTimeout(resolve, 3000));
                
            } catch (error) {
                console.error(`Error enviando a ${Nombre}:`, error.message);
            }
        }
        
        console.log('Todos los mensajes han sido enviados!');
    } catch (error) {
        console.error('Error procesando archivo:', error);
    }
}

// API REST para la interfaz web
app.use(express.json());
app.use(express.static('public'));

// Endpoint para enviar mensajes
app.post('/enviar-mensajes', upload.fields([
    { name: 'contactos', maxCount: 1 },
    { name: 'imagen', maxCount: 1 }
]), async (req, res) => {
    const { mensaje } = req.body;
    const archivoContactos = req.files.contactos[0].path;
    const imagenPath = req.files.imagen ? req.files.imagen[0].path : null;

    try {
        await enviarMensajesPersonalizados(archivoContactos, mensaje, imagenPath);
        res.json({ success: true, message: 'Mensajes enviados correctamente' });
    } catch (error) {
        res.status(500).json({ success: false, error: error.message });
    }
});

// Iniciar servidor
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Servidor corriendo en puerto ${PORT}`);
});

// Inicializar cliente WhatsApp
client.initialize();
```

#### Frontend React para la Interfaz Web

```javascript
// src/components/WhatsAppSender.js
import React, { useState } from 'react';
import axios from 'axios';

const WhatsAppSender = () => {
    const [mensaje, setMensaje] = useState('');
    const [archivoContactos, setArchivoContactos] = useState(null);
    const [imagen, setImagen] = useState(null);
    const [enviando, setEnviando] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setEnviando(true);

        const formData = new FormData();
        formData.append('mensaje', mensaje);
        formData.append('contactos', archivoContactos);
        if (imagen) formData.append('imagen', imagen);

        try {
            const response = await axios.post('/enviar-mensajes', formData, {
                headers: { 'Content-Type': 'multipart/form-data' }
            });
            
            alert('Mensajes enviados correctamente!');
        } catch (error) {
            alert('Error enviando mensajes: ' + error.response?.data?.error);
        } finally {
            setEnviando(false);
        }
    };

    return (
        <div className="container">
            <h2>Envío de Mensajes Personalizados</h2>
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <label>Mensaje:</label>
                    <textarea
                        value={mensaje}
                        onChange={(e) => setMensaje(e.target.value)}
                        placeholder="Usa {nombre} y {genero} para personalizar"
                        required
                    />
                </div>
                
                <div className="form-group">
                    <label>Archivo de Contactos (.xlsx):</label>
                    <input
                        type="file"
                        accept=".xlsx"
                        onChange={(e) => setArchivoContactos(e.target.files[0])}
                        required
                    />
                </div>
                
                <div className="form-group">
                    <label>Imagen (opcional):</label>
                    <input
                        type="file"
                        accept="image/*"
                        onChange={(e) => setImagen(e.target.files[0])}
                    />
                </div>
                
                <button type="submit" disabled={enviando}>
                    {enviando ? 'Enviando...' : 'Enviar Mensajes'}
                </button>
            </form>
        </div>
    );
};

export default WhatsAppSender;
```

### 🟡 Opción 2: PyAutoGUI + Python Web (Migración Rápida)

**Ventajas**:
- ✅ Reutilización del código existente
- ✅ Menor curva de aprendizaje
- ✅ Migración más rápida
- ✅ Mantiene la lógica actual

**Desventajas**:
- ❌ Sigue dependiendo de la interfaz gráfica
- ❌ Menos escalable
- ❌ Requiere servidor con interfaz gráfica

#### Implementación con Flask

```python
# app.py (Backend Flask)
from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import pandas as pd
import webbrowser as web
import pyautogui as pg
import time
from werkzeug.utils import secure_filename
import threading

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

# Crear directorio de uploads si no existe
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def enviar_mensajes_web(archivo_contactos, mensaje, imagen_path=None, config=None):
    """
    Versión web de la función enviar_mensajes
    """
    try:
        # Configuración por defecto
        if config is None:
            config = {
                'tiempo_carga': 15,
                'tiempo_click': 3,
                'tiempo_envio': 3,
                'tiempo_cerrar': 3,
                'click_x': 900,
                'click_y': 450
            }
        
        # Leer archivo Excel
        data = pd.read_excel(archivo_contactos, sheet_name='Personas')
        
        resultados = []
        
        for i in range(len(data)):
            try:
                celular = str(data.loc[i, 'Celular'])
                nombre = data.loc[i, 'Nombre']
                genero = data.loc[i, 'Genero']
                
                # Personalizar mensaje
                mensaje_personalizado = mensaje.replace("{nombre}", nombre).replace("{genero}", genero)
                
                # Codificar mensaje para URL
                mensaje_codificado = mensaje_personalizado.replace(" ", "%20")
                
                # Abrir WhatsApp Web
                web.open(f"https://web.whatsapp.com/send?phone={celular}&text={mensaje_codificado}")
                time.sleep(config['tiempo_carga'])
                
                # Hacer click en la caja de texto
                pg.click(config['click_x'], config['click_y'])
                time.sleep(config['tiempo_click'])
                
                # Enviar imagen si existe
                if imagen_path and os.path.exists(imagen_path):
                    # Lógica para enviar imagen (similar al código original)
                    pg.click(config['click_x']-1, config['click_y'])
                    pg.press('tab')
                    time.sleep(0.5)
                    pg.press('enter')
                    time.sleep(config['tiempo_click'])
                    
                    # Navegar a "Fotos y videos"
                    pg.press('down')
                    time.sleep(0.5)
                    pg.press('down')
                    time.sleep(0.5)
                    pg.press('enter')
                    time.sleep(config['tiempo_click'])
                    
                    # Escribir ruta de la imagen
                    ruta_normalizada = os.path.normpath(imagen_path)
                    pg.write(f'"{ruta_normalizada}"')
                    time.sleep(config['tiempo_click'])
                    
                    # Seleccionar y enviar imagen
                    pg.press('enter')
                    time.sleep(config['tiempo_envio'])
                    pg.press('enter')
                    time.sleep(config['tiempo_envio'])
                
                # Enviar mensaje
                pg.press('enter')
                time.sleep(config['tiempo_envio'])
                
                # Cerrar pestaña
                time.sleep(config['tiempo_cerrar'])
                pg.hotkey('ctrl', 'w')
                
                resultados.append({
                    'nombre': nombre,
                    'celular': celular,
                    'status': 'enviado',
                    'mensaje': 'Mensaje enviado correctamente'
                })
                
            except Exception as e:
                resultados.append({
                    'nombre': nombre if 'nombre' in locals() else 'Desconocido',
                    'celular': celular if 'celular' in locals() else 'Desconocido',
                    'status': 'error',
                    'mensaje': str(e)
                })
        
        return resultados
        
    except Exception as e:
        return [{'status': 'error', 'mensaje': f'Error general: {str(e)}'}]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar_mensajes():
    try:
        # Obtener datos del formulario
        mensaje = request.form['mensaje']
        config = {
            'tiempo_carga': int(request.form.get('tiempo_carga', 15)),
            'tiempo_click': int(request.form.get('tiempo_click', 3)),
            'tiempo_envio': int(request.form.get('tiempo_envio', 3)),
            'tiempo_cerrar': int(request.form.get('tiempo_cerrar', 3)),
            'click_x': int(request.form.get('click_x', 900)),
            'click_y': int(request.form.get('click_y', 450))
        }
        
        # Manejar archivo de contactos
        archivo_contactos = request.files['contactos']
        if archivo_contactos.filename == '':
            return jsonify({'error': 'No se seleccionó archivo de contactos'}), 400
        
        filename = secure_filename(archivo_contactos.filename)
        archivo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        archivo_contactos.save(archivo_path)
        
        # Manejar imagen opcional
        imagen_path = None
        if 'imagen' in request.files:
            imagen = request.files['imagen']
            if imagen.filename != '':
                imagen_filename = secure_filename(imagen.filename)
                imagen_path = os.path.join(app.config['UPLOAD_FOLDER'], imagen_filename)
                imagen.save(imagen_path)
        
        # Ejecutar envío en hilo separado para no bloquear la interfaz
        def ejecutar_envio():
            return enviar_mensajes_web(archivo_path, mensaje, imagen_path, config)
        
        # Para simplificar, ejecutamos directamente (en producción usar Celery)
        resultados = ejecutar_envio()
        
        return jsonify({
            'success': True,
            'message': 'Proceso completado',
            'resultados': resultados
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

#### Frontend HTML para PyAutoGUI

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WhatsApp Mensajes Personalizados - Web</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input, textarea, select {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 16px;
        }
        textarea {
            height: 100px;
            resize: vertical;
        }
        .config-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
        }
        button {
            background-color: #25D366;
            color: white;
            padding: 15px 30px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            width: 100%;
        }
        button:hover {
            background-color: #128C7E;
        }
        button:disabled {
            background-color: #ccc;
            cursor: not-allowed;
        }
        .results {
            margin-top: 20px;
            padding: 15px;
            background-color: #f8f9fa;
            border-radius: 5px;
        }
        .success { color: #28a745; }
        .error { color: #dc3545; }
    </style>
</head>
<body>
    <div class="container">
        <h1>📱 WhatsApp Mensajes Personalizados</h1>
        <p>Envía mensajes personalizados a múltiples contactos usando variables como <code>{nombre}</code> y <code>{genero}</code></p>
        
        <form id="messageForm" enctype="multipart/form-data">
            <div class="form-group">
                <label for="mensaje">Mensaje:</label>
                <textarea 
                    id="mensaje" 
                    name="mensaje" 
                    placeholder="Hola {genero} {nombre}, espero que tengas un excelente día."
                    required
                ></textarea>
            </div>
            
            <div class="form-group">
                <label for="contactos">Archivo de Contactos (.xlsx):</label>
                <input type="file" id="contactos" name="contactos" accept=".xlsx" required>
            </div>
            
            <div class="form-group">
                <label for="imagen">Imagen (opcional):</label>
                <input type="file" id="imagen" name="imagen" accept="image/*,video/*">
            </div>
            
            <h3>Configuración de Tiempos</h3>
            <div class="config-grid">
                <div class="form-group">
                    <label for="tiempo_carga">Tiempo de carga (segundos):</label>
                    <input type="number" id="tiempo_carga" name="tiempo_carga" value="15" min="1" max="60">
                </div>
                <div class="form-group">
                    <label for="tiempo_click">Tiempo entre clicks (segundos):</label>
                    <input type="number" id="tiempo_click" name="tiempo_click" value="3" min="1" max="10">
                </div>
                <div class="form-group">
                    <label for="tiempo_envio">Tiempo de envío (segundos):</label>
                    <input type="number" id="tiempo_envio" name="tiempo_envio" value="3" min="1" max="10">
                </div>
                <div class="form-group">
                    <label for="tiempo_cerrar">Tiempo para cerrar (segundos):</label>
                    <input type="number" id="tiempo_cerrar" name="tiempo_cerrar" value="3" min="1" max="10">
                </div>
            </div>
            
            <h3>Coordenadas del Click</h3>
            <div class="config-grid">
                <div class="form-group">
                    <label for="click_x">Coordenada X:</label>
                    <input type="number" id="click_x" name="click_x" value="900" min="0" max="3000">
                </div>
                <div class="form-group">
                    <label for="click_y">Coordenada Y:</label>
                    <input type="number" id="click_y" name="click_y" value="450" min="0" max="2000">
                </div>
            </div>
            
            <button type="submit" id="submitBtn">Enviar Mensajes</button>
        </form>
        
        <div id="results" class="results" style="display: none;"></div>
    </div>

    <script>
        document.getElementById('messageForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const submitBtn = document.getElementById('submitBtn');
            const results = document.getElementById('results');
            
            submitBtn.disabled = true;
            submitBtn.textContent = 'Enviando...';
            results.style.display = 'none';
            
            try {
                const formData = new FormData(this);
                const response = await fetch('/enviar', {
                    method: 'POST',
                    body: formData
                });
                
                const data = await response.json();
                
                if (data.success) {
                    results.innerHTML = '<h3 class="success">✅ Proceso completado</h3>';
                    
                    if (data.resultados && data.resultados.length > 0) {
                        results.innerHTML += '<h4>Resultados:</h4><ul>';
                        data.resultados.forEach(resultado => {
                            const clase = resultado.status === 'enviado' ? 'success' : 'error';
                            results.innerHTML += `<li class="${clase}">
                                ${resultado.nombre} (${resultado.celular}): ${resultado.mensaje}
                            </li>`;
                        });
                        results.innerHTML += '</ul>';
                    }
                } else {
                    results.innerHTML = `<h3 class="error">❌ Error: ${data.error}</h3>`;
                }
                
            } catch (error) {
                results.innerHTML = `<h3 class="error">❌ Error de conexión: ${error.message}</h3>`;
            } finally {
                submitBtn.disabled = false;
                submitBtn.textContent = 'Enviar Mensajes';
                results.style.display = 'block';
            }
        });
    </script>
</body>
</html>
```

## 🔧 Solución de Problemas

### Problemas Comunes

#### 1. Error: "No se puede encontrar el archivo Excel"
**Solución**: Asegúrate de que el archivo `Contactos.xlsx` esté en la misma carpeta que los scripts Python.

#### 2. Error: "PyAutoGUI no funciona"
**Solución**: 
- En Linux: `sudo apt-get install python3-tk`
- En Windows: Reinstalar Python con opción "Add to PATH"

#### 3. WhatsApp Web no responde
**Solución**: 
- Ajustar las coordenadas de click en la interfaz
- Aumentar los tiempos de espera
- Verificar que estés logueado en WhatsApp Web

#### 4. Mensajes no se personalizan
**Solución**: 
- Verificar que el archivo Excel tenga las columnas: `Nombre`, `Celular`, `Genero`
- Asegurarse de usar `{nombre}` y `{genero}` en el mensaje

### Logs y Debugging

Para activar logs detallados, edita `app.py` y añade:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Para contribuir:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

### Desarrollo Local

```bash
# Clonar el repositorio
git clone https://github.com/usuario/WhatsApp-Mensajes-Personalizados.git
cd WhatsApp-Mensajes-Personalizados

# Instalar dependencias de desarrollo
pip install -r requirements-dev.txt

# Ejecutar tests
python -m pytest tests/

# Ejecutar linter
flake8 *.py
```

## 📄 Licencia

Este proyecto está bajo la Licencia GPL-3.0. Ver el archivo [LICENSE](LICENSE) para más detalles.

## ⚠️ Aviso Legal

Este proyecto es para fines educativos y de automatización personal. El uso de este software debe cumplir con:

- Los términos de servicio de WhatsApp
- Las leyes locales sobre privacidad y comunicaciones
- El consentimiento de los destinatarios de los mensajes

**No nos hacemos responsables del uso indebido de esta herramienta.**

## 🔗 Enlaces Útiles

- [WhatsApp Terms of Service](https://www.whatsapp.com/legal/terms-of-service)
- [Python Official Documentation](https://docs.python.org/3/)
- [PyAutoGUI Documentation](https://pyautogui.readthedocs.io/)
- [whatsapp-web.js Documentation](https://wwebjs.dev/)

---

<p align="center">
  Desarrollado con ❤️ para automatizar tus mensajes de WhatsApp
</p>