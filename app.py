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
    mensaje = "Hola " + genero + " " + nombre + ", buenas noches 👋🏻. Espero que estés teniendo un feliz final de semana." + "%0D%0A%0D%0A" + "Quiero contarte que el próximo sábado estaremos teniendo nuestro *#SábadoMiraísta,* en donde tendremos un encuentro para destacar la labor de nuestros ```Adultos Mayores en Carvajal``` 👵🏻👴🏼. Se llevará a cabo así:" + "%0D%0A" + "* 🗓️ sábado 28 de septiembre de 2024" + "%0D%0A" + "* 🕑 2:00 pm" + "%0D%0A" + "* 📍 parqueadero Carvajal (Av. Boyacá # 35 - 43 Sur)" + "%0D%0A" + "* 🌎 https://maps.app.goo.gl/zDBNYGgx6MpgNSid8" + "%0D%0A%0D%0A" + "🫵🏻 Nos gustaría contar con tu apoyo con toda la preparación o con la ejecución de la actividad, anímate a colaborarnos en algunas de las siguientes actividades." + "%0D%0A%0D%0A" + "*A. Llamar a los invitados ☎️:* necesitamos contactar a la mayor cantidad de hermanos adultos mayores, para que ninguno se pierda esta ocasión. (desde el lunes 23 hasta el miércoles 25 de septiembre)." + "%0D%0A%0D%0A" + "*B. Preparar el lugar 🎈:* buscaremos garantizar que todos los asistentes se sientan cómodos y agusto con el lugar de reunión (sábado 28 de septiembre desde las 7:30 hasta las 11:00 am)." + "%0D%0A%0D%0A" + "*C. Acompañar el evento 🎤:* al ser nuestros invitados especiales adultos mayores, queremos darles todo el apoyo y acompañamiento posible en las actividades que se llevarán a cabo (sábado 28 de septiembre desde la 1:30 hasta las 4:30 pm)." + "%0D%0A%0D%0A" + "🙋🏻‍♂️🙋🏼‍♀️ Coméntame en cuáles de estas tres opciones A, B o C podrías darnos una mano. También entendemos los compromisos que puedas tener, coméntame también si tienes difícultades para apoyarnos." + "%0D%0A%0D%0A" + "Gracias por tu atención. Te deseo un buen inicio de semana." + "%0D%0A%0D%0A" + "> att: Sebastian Romero (Responsable de InfoMIRA en Carvajal)"
    
    # Abrir una nueva pestaña para entrar a WhatsApp Web
    # Opción 1: Si te abre WhastApp Web directamente en Google Chrome
    web.open("https://web.whatsapp.com/send?phone=" + celular + "&text=" + mensaje)

    # Opción 2: Si te abre WhastApp Web en Microsoft Edge, especificar que lo abra en Chrome
    # chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    # web.get(chrome_path).open("https://web.whatsapp.com/send?phone=" + celular + "&text=" + mensaje)

    time.sleep(8)           # Esperar 8 segundos a que cargue
    pg.click(1040,590)      # Hacer click en la caja de texto
    time.sleep(2)           # Esperar 2 segundos
    pg.press('enter')       # Enviar mensaje
    time.sleep(2)           # Esperar 2 segundos a que se envíe el mensaje
    pg.hotkey('ctrl', 'w')  # Cerrar la pestaña

