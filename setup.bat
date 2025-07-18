@echo off
setlocal enabledelayedexpansion

:: Configurar colores para Windows
:: Usar powershell para colores si está disponible
powershell -Command "Write-Host ''" >nul 2>&1
if %errorlevel% equ 0 (
    set "COLOR_ENABLED=1"
) else (
    set "COLOR_ENABLED=0"
)

:: Funciones para mostrar mensajes con colores
:print_status
if "%COLOR_ENABLED%"=="1" (
    powershell -Command "Write-Host '[INFO] %~1' -ForegroundColor Cyan"
) else (
    echo [INFO] %~1
)
goto :eof

:print_success
if "%COLOR_ENABLED%"=="1" (
    powershell -Command "Write-Host '[EXITO] %~1' -ForegroundColor Green"
) else (
    echo [EXITO] %~1
)
goto :eof

:print_warning
if "%COLOR_ENABLED%"=="1" (
    powershell -Command "Write-Host '[ADVERTENCIA] %~1' -ForegroundColor Yellow"
) else (
    echo [ADVERTENCIA] %~1
)
goto :eof

:print_error
if "%COLOR_ENABLED%"=="1" (
    powershell -Command "Write-Host '[ERROR] %~1' -ForegroundColor Red"
) else (
    echo [ERROR] %~1
)
goto :eof

:: Verificar si Python está instalado
call :print_status "Verificando si Python esta instalado..."
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    call :print_error "Python no esta instalado. Iniciando la descarga e instalacion de Python..."
    
    :: Verificar si curl está disponible
    curl --version >nul 2>&1
    IF %ERRORLEVEL% NEQ 0 (
        call :print_error "curl no esta disponible. Descarga Python manualmente desde https://www.python.org/downloads/"
        pause
        exit /b 1
    )
    
    :: Descargar Python desde la web oficial
    call :print_status "Descargando Python 3.11..."
    curl -o python-installer.exe https://www.python.org/ftp/python/3.11.6/python-3.11.6-amd64.exe
    
    IF %ERRORLEVEL% NEQ 0 (
        call :print_error "Error al descargar Python. Verifica tu conexion a internet."
        pause
        exit /b 1
    )
    
    :: Instalar Python silenciosamente y añadirlo al PATH
    call :print_status "Instalando Python..."
    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

    :: Comprobar si la instalación fue exitosa
    python --version >nul 2>&1
    IF %ERRORLEVEL% NEQ 0 (
        call :print_error "Python no pudo ser instalado correctamente."
        pause
        exit /b 1
    )
    
    call :print_success "Python instalado correctamente."
    
    :: Limpiar el instalador
    del python-installer.exe >nul 2>&1
) else (
    for /f "tokens=*" %%i in ('python --version 2^>^&1') do set "PYTHON_VERSION=%%i"
    call :print_success "Python esta instalado: !PYTHON_VERSION!"
)

:: Verificar si pip está disponible
call :print_status "Verificando pip..."
python -m pip --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    call :print_warning "pip no encontrado. Instalando pip..."
    python -m ensurepip --upgrade
    IF %ERRORLEVEL% NEQ 0 (
        call :print_error "Error al instalar pip."
        pause
        exit /b 1
    )
)

:: Actualizar pip a la última versión
call :print_status "Actualizando pip a la ultima version..."
python -m pip install --upgrade pip
IF %ERRORLEVEL% NEQ 0 (
    call :print_warning "No se pudo actualizar pip, continuando..."
)

:: Instalar el paquete wheel
call :print_status "Instalando el paquete wheel para prevenir problemas de instalacion..."
python -m pip install wheel
IF %ERRORLEVEL% NEQ 0 (
    call :print_warning "No se pudo instalar wheel, continuando..."
)

:: Crear el entorno virtual 'venv' si no existe
call :print_status "Configurando entorno virtual..."
IF NOT EXIST "venv" (
    call :print_status "Creando el entorno virtual 'venv'..."
    python -m venv venv
    IF %ERRORLEVEL% NEQ 0 (
        call :print_error "Error al crear el entorno virtual."
        pause
        exit /b 1
    )
    call :print_success "Entorno virtual creado."
) else (
    call :print_warning "El entorno virtual ya existe."
)

:: Activar el entorno virtual
call :print_status "Activando el entorno virtual..."
call venv\Scripts\activate
IF %ERRORLEVEL% NEQ 0 (
    call :print_error "Error al activar el entorno virtual."
    pause
    exit /b 1
)

:: Actualizar pip dentro del entorno virtual
call :print_status "Actualizando pip en el entorno virtual..."
python -m pip install --upgrade pip

:: Verificar que requirements.txt existe
IF NOT EXIST "requirements.txt" (
    call :print_error "Archivo requirements.txt no encontrado."
    pause
    exit /b 1
)

:: Instalar dependencias desde requirements.txt
call :print_status "Instalando dependencias necesarias desde requirements.txt..."
pip install -r requirements.txt
IF %ERRORLEVEL% NEQ 0 (
    call :print_error "Error al instalar las dependencias."
    pause
    exit /b 1
)

:: Verificar que las dependencias principales estén instaladas
call :print_status "Verificando instalacion de dependencias criticas..."
python -c "import tkinter; import pandas; import pyautogui; import openpyxl" >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    call :print_error "Algunas dependencias criticas no se instalaron correctamente."
    pause
    exit /b 1
) else (
    call :print_success "Todas las dependencias criticas estan instaladas."
)

:: Verificar archivo de contactos
call :print_status "Verificando archivo de contactos..."
IF NOT EXIST "Contactos.xlsx" (
    call :print_warning "Archivo Contactos.xlsx no encontrado. Asegurate de tener tu archivo de contactos."
)

call :print_success "¡Instalacion completada con exito!"
echo.
if "%COLOR_ENABLED%"=="1" (
    powershell -Command "Write-Host '═══════════════════════════════════════════════════════════' -ForegroundColor Green"
    powershell -Command "Write-Host '  CONFIGURACION COMPLETADA - LISTO PARA USAR' -ForegroundColor Green"
    powershell -Command "Write-Host '═══════════════════════════════════════════════════════════' -ForegroundColor Green"
) else (
    echo ═══════════════════════════════════════════════════════════
    echo   CONFIGURACION COMPLETADA - LISTO PARA USAR
    echo ═══════════════════════════════════════════════════════════
)
echo.
echo Para ejecutar el programa:
echo 1. Activa el entorno virtual: venv\Scripts\activate
echo 2. Ejecuta la aplicacion: python gui.py
echo.
echo O ejecuta directamente: run.bat
echo.

:: Crear script de ejecución rápida
call :print_status "Creando script de ejecucion rapida..."
echo @echo off > run.bat
echo :: Script de ejecucion rapida para WhatsApp Mensajes Personalizados >> run.bat
echo. >> run.bat
echo :: Activar entorno virtual >> run.bat
echo call venv\Scripts\activate >> run.bat
echo. >> run.bat
echo :: Ejecutar la aplicacion >> run.bat
echo python gui.py >> run.bat
echo. >> run.bat
echo pause >> run.bat

call :print_success "Script de ejecucion rapida creado: run.bat"
echo.
call :print_success "¡Todo listo! Puedes ejecutar 'run.bat' para iniciar la aplicacion."

pause
