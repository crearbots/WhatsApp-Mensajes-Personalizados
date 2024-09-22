@echo off
echo.
echo Actualizando el entorno y creando el entorno virtual...
python -m venv venv

echo.
echo Activando el entorno virtual...
call venv\Scripts\activate

echo.
echo Instalando dependencias necesarias...
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo Instalación completada. Puedes ejecutar el programa con 'python app.py'.
pause

