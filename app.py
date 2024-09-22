import pandas as pd
import webbrowser as web
import pyautogui as pg
import time

data = pd.read_excel("Contactos.xlsx", sheet_name='Personas')

for i in range(len(data)):
    celular = data.loc[i,'Celular'].astype(str) # Convertir a string para que se añada al mensaje
    nombre = data.loc[i,'Nombre']
    genero = data.loc[i,'Genero']

    # Crear mensaje personalizado
    mensaje = "Mucho gusto " + genero + " " + nombre + ", mi nombre es Sebastian Romero, que gusto escribirle 🙌"

    # Abrir una nueva pestaña para entrar a WhatsApp Web
    # Opción 1: Si te abre WhastApp Web directamente en Google Chrome
    web.open("https://web.whatsapp.com/send?phone=" + celular + "&text=" + mensaje)

    # Opción 2: Si te abre WhastApp Web en Microsoft Edge, especificar que lo abra en Chrome
    # chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    # web.get(chrome_path).open("https://web.whatsapp.com/send?phone=" + celular + "&text=" + mensaje)

    time.sleep(8)           # Esperar 8 segundos a que cargue
    pg.click(1230,964)      # Hacer click en la caja de texto
    time.sleep(2)           # Esperar 2 segundos
    pg.press('enter')       # Enviar mensaje
    time.sleep(3)           # Esperar 3 segundos a que se envíe el mensaje
    pg.hotkey('ctrl', 'w')  # Cerrar la pestaña
    time.sleep(2)

