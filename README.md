# Guía para ejecutar el programa de envío de mensajes por WhatsApp

¡Bienvenido! Este programa te permitirá enviar mensajes de WhatsApp de manera automática utilizando una lista de contactos que puedes modificar en un archivo llamado `Contactos.xlsx`. No te preocupes si nunca has tocado una línea de código, esta guía te llevará paso a paso para que puedas ejecutar el programa sin problemas.

## Requisitos previos

Antes de comenzar, asegúrate de cumplir con los siguientes requisitos:

1. **Instalar Python**: Python es un lenguaje de programación necesario para ejecutar este programa.
   - Si ya tienes Python instalado, ¡puedes pasar al siguiente paso!
   - Si **no tienes Python instalado**, sigue estos pasos:
   
   ### Cómo instalar Python en Windows:

   1. Ve al sitio web oficial de Python: [https://www.python.org/downloads/](https://www.python.org/downloads/).
   2. Haz clic en el botón amarillo que dice **Download Python [versión]** (Asegúrate de que la versión sea 3.x.x, no importa el número exacto).
   3. Abre el archivo descargado y asegúrate de **marcar la casilla** que dice **"Add Python to PATH"** antes de hacer clic en **Install Now**.
   4. Una vez que termine la instalación, verifica que está instalado correctamente:
      - Abre el **Símbolo del sistema** (puedes buscarlo como "cmd" en el menú de inicio).
      - Escribe `python --version` y presiona **Enter**. Deberías ver algo como `Python 3.x.x`.

2. **Acceder a WhatsApp Web**:
   - Asegúrate de estar **logueado en WhatsApp Web** usando Google Chrome:
     - Ve a [https://web.whatsapp.com](https://web.whatsapp.com) en tu navegador Google Chrome.
     - Escanea el código QR con tu teléfono para vincular tu cuenta de WhatsApp.
   
## Pasos para configurar y ejecutar el programa

A continuación, se presentan los pasos para que tu equipo esté listo para ejecutar el programa. Hemos creado un script que automatiza gran parte de la instalación, así que no te preocupes por los detalles técnicos.

### 1. Descarga y prepara el entorno de tu proyecto

1. Descarga el proyecto de la siguiente manera:
   - [Descargar el archivo ZIP](#) o clonar el repositorio si tienes Git instalado.
   - Descomprime el archivo en una carpeta de tu preferencia.

2. En la carpeta del proyecto, verás un archivo llamado `setup.bat`. Este archivo instalará todas las dependencias necesarias para que puedas ejecutar el programa.

3. Haz doble clic en el archivo `setup.bat`. **Este paso es importante ya que preparará tu entorno**:
   - Creará un entorno virtual para Python.
   - Instalará todas las librerías que el programa necesita.

### 2. Modifica la lista de contactos

1. En la carpeta del proyecto, encontrarás un archivo llamado `Contactos.xlsx`.
   - Este archivo contiene la lista de contactos a los que se les enviará un mensaje.
   - Abre el archivo en Excel y **añade los nombres y números de teléfono** en el formato correcto (Asegúrate de que el formato del número esté completo, incluyendo el código de país).

### 3. Ejecutar el programa

1. Abre el **Símbolo del sistema** de nuevo.
2. Navega hasta la carpeta donde está el proyecto (la misma donde se encuentra el archivo `app.py`).
   - Puedes usar el comando `cd` en el terminal. Por ejemplo:
     ```bash
     cd C:\ruta\a\tu\carpeta\del\proyecto
     ```
3. Ejecuta el siguiente comando para iniciar el programa:
   ```bash
   python app.py

