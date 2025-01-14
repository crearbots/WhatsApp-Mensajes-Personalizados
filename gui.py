import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import subprocess
from app import enviar_mensajes  # Importar la función desde app.py
from mensaje import obtener_mensaje  # Importamos la función para abrir la ventana de mensaje

# Función para seleccionar el archivo de contactos
def seleccionar_archivo():
    archivo = filedialog.askopenfilename(
        title="Seleccionar archivo de Contactos",
        filetypes=(("Archivos Excel", "*.xlsx"), ("Todos los archivos", "*.*"))
    )
    if archivo:
        ruta_contactos.set(archivo)

# Función para seleccionar la imagen o video a enviar
def seleccionar_imagen():
    imagen = filedialog.askopenfilename(
        title="Seleccionar imagen o video para adjuntar",
        filetypes=(("Imágenes y Videos", "*.png;*.jpg;*.jpeg;*.gif;*.mp4;*.mov;*.avi"), ("Todos los archivos", "*.*"))
    )
    if imagen:
        ruta_imagen.set(imagen)

# Callback para recibir el mensaje procesado desde mensaje.py
def recibir_mensaje(mensaje):
    ventana.mensaje = mensaje  # Guardar el mensaje en la ventana principal
    print(f"Mensaje recibido y procesado: {mensaje}")  # Imprimir el mensaje para confirmar que llega

# Función para ejecutar el script de envío
def ejecutar_envio():
    archivo = ruta_contactos.get()
    imagen = ruta_imagen.get()

    if not archivo:
        messagebox.showerror("Error", "Por favor, selecciona el archivo de contactos.")
        return

    if not archivo.endswith(".xlsx"):
        messagebox.showerror("Error", "El archivo seleccionado no es un archivo Excel válido.")
        return

    # Obtener los parámetros personalizados del usuario
    try:
        tiempo_carga = int(entrada_tiempo_carga.get())
        tiempo_click = int(entrada_tiempo_click.get())
        tiempo_envio = int(entrada_tiempo_envio.get())
        tiempo_cerrar = int(entrada_tiempo_cerrar.get())
        click_x = int(entrada_click_x.get())
        click_y = int(entrada_click_y.get())
        
        # Copiar el archivo seleccionado y renombrarlo a Contactos.xlsx
        shutil.copy(archivo, "Contactos.xlsx")
        
        # Verificar que el mensaje esté disponible
        if not hasattr(ventana, 'mensaje'):
            messagebox.showerror("Error", "Por favor, escribe y confirma un mensaje para enviar.")
            return
        
        # Ejecutar la función enviar_mensajes con los valores personalizados
        enviar_mensajes(tiempo_carga, tiempo_click, tiempo_envio, tiempo_cerrar, click_x, click_y, ventana.mensaje, imagen)
        messagebox.showinfo("Éxito", "El envío de mensajes ha comenzado correctamente.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al ejecutar el script: {str(e)}")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Envío de Mensajes por WhatsApp")
ventana.geometry("500x850")

ruta_contactos = tk.StringVar()  # Variable para almacenar la ruta del archivo de contactos
ruta_imagen = tk.StringVar()     # Variable para almacenar la ruta de la imagen seleccionada

# Etiqueta y botón para seleccionar el archivo de contactos
label_archivo = tk.Label(ventana, text="Seleccionar archivo de contactos (Excel):")
label_archivo.pack(pady=10)

entrada_archivo = tk.Entry(ventana, textvariable=ruta_contactos, width=50)
entrada_archivo.pack(pady=5)

boton_seleccionar = tk.Button(ventana, text="Seleccionar archivo", command=seleccionar_archivo)
boton_seleccionar.pack(pady=5)

# Botón para abrir la ventana del mensaje
boton_mensaje = tk.Button(ventana, text="Escribir Mensaje", command=lambda: obtener_mensaje(recibir_mensaje))
boton_mensaje.pack(pady=10)

# Etiqueta y botón para seleccionar la imagen a adjuntar
label_imagen = tk.Label(ventana, text="Seleccionar imagen o video para adjuntar:")
label_imagen.pack(pady=10)

entrada_imagen = tk.Entry(ventana, textvariable=ruta_imagen, width=50)
entrada_imagen.pack(pady=5)

boton_seleccionar_imagen = tk.Button(ventana, text="Seleccionar imagen o video", command=seleccionar_imagen)
boton_seleccionar_imagen.pack(pady=5)

# Entradas para modificar los tiempos de espera y las coordenadas
label_tiempos = tk.Label(ventana, text="Configurar tiempos de espera (en segundos):\nTiempo para cargar WhatsApp Web")
label_tiempos.pack(pady=5)

entrada_tiempo_carga = tk.Entry(ventana, width=10)
entrada_tiempo_carga.insert(0, "10")  # Valor por defecto
entrada_tiempo_carga.pack(pady=5)
label_carga = tk.Label(ventana, text="Tiempo entre click y escribir mensaje")
label_carga.pack()

entrada_tiempo_click = tk.Entry(ventana, width=10)
entrada_tiempo_click.insert(0, "3")  # Valor por defecto
entrada_tiempo_click.pack(pady=5)
label_click = tk.Label(ventana, text="Tiempo entre enviar mensaje/vídeo")
label_click.pack()

entrada_tiempo_envio = tk.Entry(ventana, width=10)
entrada_tiempo_envio.insert(0, "3")  # Valor por defecto
entrada_tiempo_envio.pack(pady=5)
label_envio = tk.Label(ventana, text="Tiempo para cerrar pestaña")
label_envio.pack()

entrada_tiempo_cerrar = tk.Entry(ventana, width=10)
entrada_tiempo_cerrar.insert(0, "0")  # Valor por defecto
entrada_tiempo_cerrar.pack(pady=5)

# Entradas para modificar las coordenadas del click
label_coordenadas = tk.Label(ventana, text="Configurar coordenadas del click (X, Y):\nPosición X del click")
label_coordenadas.pack(pady=5)

entrada_click_x = tk.Entry(ventana, width=10)
entrada_click_x.insert(0, "900")  # Valor por defecto
entrada_click_x.pack(pady=5)
label_x = tk.Label(ventana, text="Posición Y del click")
label_x.pack()

entrada_click_y = tk.Entry(ventana, width=10)
entrada_click_y.insert(0, "450")  # Valor por defecto
entrada_click_y.pack(pady=5)
label_y = tk.Label(ventana, text="")
label_y.pack()

# Botón para iniciar el envío de mensajes
boton_enviar = tk.Button(ventana, text="Iniciar envío de mensajes", command=ejecutar_envio)
boton_enviar.pack(pady=20)

# Iniciar el loop de la ventana
ventana.mainloop()
