#!/bin/bash

# Colores para mejor visualización
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Función para mostrar mensajes con color
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[ÉXITO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[ADVERTENCIA]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Verificar si Python3 está instalado
print_status "Verificando si Python3 está instalado..."
if ! command -v python3 &> /dev/null; then
    print_error "Python3 no está instalado. Instalando Python3..."
    
    # Detectar la distribución de Linux
    if [[ -f /etc/debian_version ]]; then
        # Debian/Ubuntu
        sudo apt-get update
        sudo apt-get install -y python3 python3-pip python3-venv python3-tk python3-dev
    elif [[ -f /etc/redhat-release ]]; then
        # Red Hat/CentOS/Fedora
        sudo yum install -y python3 python3-pip python3-tkinter python3-devel
    elif [[ -f /etc/arch-release ]]; then
        # Arch Linux
        sudo pacman -S python python-pip tk
    else
        print_error "Distribución de Linux no soportada. Instala Python3 manualmente."
        exit 1
    fi
else
    print_success "Python3 está instalado: $(python3 --version)"
fi

# Verificar si pip está instalado
print_status "Verificando pip..."
if ! command -v pip3 &> /dev/null; then
    print_warning "pip3 no encontrado. Instalando pip..."
    python3 -m ensurepip --upgrade
fi

# Actualizar los paquetes del sistema
print_status "Actualizando lista de paquetes del sistema..."
if [[ -f /etc/debian_version ]]; then
    sudo apt-get update
    sudo apt-get install -y python3-tk python3-dev build-essential
elif [[ -f /etc/redhat-release ]]; then
    sudo yum update -y
    sudo yum install -y python3-tkinter python3-devel gcc
elif [[ -f /etc/arch-release ]]; then
    sudo pacman -Syu
    sudo pacman -S tk base-devel
fi

# Crear el entorno virtual si no existe
print_status "Configurando entorno virtual..."
if [ ! -d "venv" ]; then
    print_status "Creando entorno virtual 'venv'..."
    python3 -m venv venv
    print_success "Entorno virtual creado."
else
    print_warning "El entorno virtual ya existe."
fi

# Activar el entorno virtual
print_status "Activando el entorno virtual..."
source venv/bin/activate

# Actualizar pip dentro del entorno virtual
print_status "Actualizando pip..."
python -m pip install --upgrade pip

# Instalar wheel para evitar problemas de compilación
print_status "Instalando wheel..."
pip install wheel

# Instalar las dependencias de Python
print_status "Instalando dependencias de Python desde requirements.txt..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    print_success "Dependencias instaladas correctamente."
else
    print_error "Archivo requirements.txt no encontrado."
    exit 1
fi

# Verificar que las dependencias principales estén instaladas
print_status "Verificando instalación de dependencias críticas..."
python -c "import tkinter; import pandas; import pyautogui; import openpyxl" 2>/dev/null
if [ $? -eq 0 ]; then
    print_success "Todas las dependencias críticas están instaladas."
else
    print_error "Algunas dependencias críticas no se instalaron correctamente."
    exit 1
fi

# Crear archivo de verificación de contactos si no existe
print_status "Verificando archivo de contactos..."
if [ ! -f "Contactos.xlsx" ]; then
    print_warning "Archivo Contactos.xlsx no encontrado. Asegúrate de tener tu archivo de contactos."
fi

print_success "¡Instalación completada con éxito!"
echo ""
echo -e "${GREEN}═══════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}  CONFIGURACIÓN COMPLETADA - LISTO PARA USAR${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${BLUE}Para ejecutar el programa:${NC}"
echo -e "${YELLOW}1.${NC} Activa el entorno virtual: ${GREEN}source venv/bin/activate${NC}"
echo -e "${YELLOW}2.${NC} Ejecuta la aplicación: ${GREEN}python3 gui.py${NC}"
echo ""
echo -e "${BLUE}O ejecuta directamente:${NC}"
echo -e "${GREEN}./run.sh${NC}"
echo ""

# Crear script de ejecución rápida
print_status "Creando script de ejecución rápida..."
cat > run.sh << 'EOF'
#!/bin/bash
# Script de ejecución rápida para WhatsApp Mensajes Personalizados

# Activar entorno virtual
source venv/bin/activate

# Ejecutar la aplicación
python3 gui.py
EOF

chmod +x run.sh
print_success "Script de ejecución rápida creado: run.sh"

