import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess

# Función para seleccionar el archivo de contactos
def seleccionar_archivo():
    archivo = filedialog.askopenfilename(
        title="Seleccionar archivo de Contactos",
        filetypes=(("Archivos Excel", "*.xlsx"), ("Todos los archivos", "*.*"))
    )
    if archivo:
        ruta_contactos.set(archivo)

# Función para ejecutar el script de envío
def ejecutar_envio():
    archivo = ruta_contactos.get()
    if not archivo:
        messagebox.showerror("Error", "Por favor, selecciona el archivo de contactos.")
        return

    # Comprobar si el archivo seleccionado es válido
    if not archivo.endswith(".xlsx"):
        messagebox.showerror("Error", "El archivo seleccionado no es un archivo Excel válido.")
        return

    # Establecer la ruta del archivo Contactos.xlsx en app.py
    try:
        # Copiar el archivo seleccionado como "Contactos.xlsx" para que sea usado por app.py
        os.replace(archivo, "Contactos.xlsx")

        # Ejecutar el script app.py
        subprocess.run(["python", "app.py"], check=True)
        messagebox.showinfo("Éxito", "El envío de mensajes ha comenzado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al ejecutar el script: {str(e)}")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Envío de Mensajes por WhatsApp")
ventana.geometry("500x200")

# Ruta del archivo seleccionada
ruta_contactos = tk.StringVar()

# Etiqueta y botón para seleccionar el archivo de contactos
label = tk.Label(ventana, text="Seleccionar archivo de contactos (Excel):")
label.pack(pady=10)

entrada = tk.Entry(ventana, textvariable=ruta_contactos, width=50)
entrada.pack(pady=5)

boton_seleccionar = tk.Button(ventana, text="Seleccionar archivo", command=seleccionar_archivo)
boton_seleccionar.pack(pady=5)

# Botón para iniciar el envío de mensajes
boton_enviar = tk.Button(ventana, text="Iniciar envío de mensajes", command=ejecutar_envio)
boton_enviar.pack(pady=20)

# Iniciar el loop de la ventana
ventana.mainloop()
