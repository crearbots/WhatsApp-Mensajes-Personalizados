#!/bin/bash

# 1. Actualizar los paquetes
echo "Actualizando lista de paquetes..."
sudo apt-get update

# 2. Instalar dependencias del sistema
echo "Instalando dependencias del sistema (python3-tk, python3-dev)..."
sudo apt-get install -y python3-tk python3-dev

# 3. Crear un entorno virtual
echo "Creando entorno virtual 'venv'..."
python3 -m venv venv

# 4. Activar el entorno virtual
echo "Activando el entorno virtual..."
source venv/bin/activate

# 5. Instalar las dependencias de Python
echo "Instalando dependencias de Python desde requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Instalación completada con éxito. ¡Estás listo para ejecutar el programa!"

