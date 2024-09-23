@echo off
echo.
echo Actualizando pip a la última versión...
python -m pip install --upgrade pip

echo.
echo Instalando el paquete wheel para prevenir problemas de instalación...
pip install wheel

echo.
echo Creando el entorno virtual 'venv'...
python -m venv venv

echo.
echo Activando el entorno virtual...
call venv\Scripts\activate

echo.
echo Instalando dependencias necesarias desde requirements.txt...
pip install -r requirements.txt

echo.
echo Instalación completada. Iniciando el programa...
python gui.py  # Ejecutar la interfaz gráfica directamente
pause
