import pandas as pd
import webbrowser as web
import pyautogui as pg
import time
import os

# Ahora estos valores vendrán como parámetros de la interfaz gráfica
def enviar_mensajes(tiempo_carga, tiempo_click, tiempo_envio, tiempo_cerrar, click_x, click_y, mensaje, ruta_imagen):
    data = pd.read_excel("Contactos.xlsx", sheet_name='Personas')

    for i in range(len(data)):
        celular = data.loc[i,'Celular'].astype(str) 
        nombre = data.loc[i,'Nombre']
        genero = data.loc[i,'Genero']
        
        # Reemplazar las variables {nombre} y {genero} en el mensaje
        mensaje_personalizado = mensaje.replace("{nombre}", nombre).replace("{genero}", genero)

        # Abrir WhatsApp Web
        web.open("https://web.whatsapp.com/send?phone=" + celular + "&text=" + mensaje_personalizado)
        time.sleep(tiempo_carga)    # Esperar a que WhatsApp Web cargue
        
        # Simular clic en la caja de texto para escribir el mensaje (ajusta las coordenadas según la pantalla)
        pg.click(click_x, click_y)  # Hacer click en la caja de texto
        time.sleep(tiempo_click)    # Esperar después del click
        pg.press('enter')           # Enviar mensaje
        time.sleep(tiempo_envio)    # Esperar a que se envíe el mensaje

        # Enviar la imagen adjunta si la ruta de imagen está disponible
        if ruta_imagen and os.path.exists(ruta_imagen):
            print("Entre al IF")
            # Simular dos veces TAB para acceder al botón de "Adjuntar"
            pg.press('tab')  # Primer TAB
            time.sleep(0.5)
            pg.press('tab')  # Segundo TAB
            time.sleep(0.5)
            # Presionar ENTER para abrir la ventana de adjuntar archivos
            pg.press('enter')
            time.sleep(tiempo_click)
            
            # Simular dos veces DOWN para seleccionar "Fotos y videos"
            pg.press('down')  # Primer DOWN
            time.sleep(0.5)
            pg.press('down')  # Segundo DOWN
            time.sleep(0.5)

            # Presionar ENTER para seleccionar "Fotos y videos"
            pg.press('enter')
            time.sleep(tiempo_click)

            # Escribir la ruta del archivo con el formato correcto para Windows
            ruta_imagen = os.path.normpath(ruta_imagen)  # Convertir la ruta a formato Windows
            print('"' + ruta_imagen + '"')  # Mostrar la ruta en la terminal
            pg.write('"' + ruta_imagen + '"')  # Escribir la ruta entre comillas
            time.sleep(tiempo_click)

            # Presionar 'Enter' para seleccionar la imagen
            pg.press('enter')
            time.sleep(tiempo_envio)

            # Presionar 'Enter' nuevamente para enviar la imagen
            pg.press('enter')
            time.sleep(tiempo_envio)
        
        # Cerrar la pestaña de WhatsApp Web
        pg.hotkey('ctrl', 'w')      # Cerrar la pestaña
        time.sleep(tiempo_cerrar)   # Esperar antes de cerrar la pestaña