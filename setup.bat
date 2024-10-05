@echo off

:: Comprobar si Python está instalado
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo.
    echo Python no esta instalado. Iniciando la descarga e instalacion de Python...
    
    :: Descargar Python desde la web oficial
    echo Descargando Python 3.11...
    curl -o python-installer.exe https://www.python.org/ftp/python/3.11.6/python-3.11.6-amd64.exe
    
    :: Instalar Python silenciosamente y añadirlo al PATH
    echo Instalando Python...
    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

    :: Comprobar si la instalación fue exitosa
    python --version >nul 2>&1
    IF %ERRORLEVEL% NEQ 0 (
        echo Error: Python no pudo ser instalado.
        pause
        exit /b 1
    )
    
    echo Python instalado correctamente.
)

:: Actualizar pip a la última versión
echo.
echo Actualizando pip a la ultima version...
python -m ensurepip --upgrade
python -m pip install --upgrade pip

:: Instalar el paquete wheel
echo.
echo Instalando el paquete wheel para prevenir problemas de instalacion...
python -m pip install wheel

:: Crear el entorno virtual 'venv'
echo.
echo Creando el entorno virtual 'venv'...
python -m venv venv

:: Activar el entorno virtual
echo.
echo Activando el entorno virtual...
call venv\Scripts\activate

:: Instalar dependencias desde requirements.txt
echo.
echo Instalando dependencias necesarias desde requirements.txt...
pip install -r requirements.txt

:: Iniciar la interfaz gráfica
echo.
echo Instalacion completada. Iniciando el programa...
python gui.py

pause
