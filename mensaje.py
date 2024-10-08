import tkinter as tk
from tkinter import messagebox
import urllib.parse

# Esta función abre la ventana para que el usuario escriba su mensaje y lo retorna validado
def obtener_mensaje(callback):
    # Función para confirmar el mensaje y procesarlo
    def confirmar_mensaje():
        mensaje = campo_texto.get("1.0", "end-1c")  # Obtener el mensaje del campo de texto
        if not mensaje:
            messagebox.showerror("Error", "El mensaje no puede estar vacío.")
        else:
            # Codificar caracteres especiales en el mensaje
            mensaje = mensaje.replace("%", "%25")
            mensaje = mensaje.replace("&", "%26")
            mensaje = mensaje.replace("#", "%23")
            mensaje = mensaje.replace("/", "%2F")
            mensaje = mensaje.replace("\\", "%5C")
            mensaje = mensaje.replace("|", "%7C")
            mensaje = mensaje.replace("$", "%24")
            mensaje = mensaje.replace("*", "%2A")
            mensaje = mensaje.replace("+", "%2B")
            mensaje = mensaje.replace("=", "%3D")
            mensaje = mensaje.replace("@", "%40")
            mensaje = mensaje.replace("?", "%3F")
            mensaje = mensaje.replace("¡", "%C2%A1")
            mensaje = mensaje.replace("¿", "%C2%BF")

            # Convertir saltos de línea en %0D%0A
            mensaje = mensaje.replace("\n", "%0D%0A") 

            ventana_mensaje.destroy()  # Cerrar la ventana después de confirmar
            callback(mensaje)  # Devolver el mensaje validado al archivo gui.py

    # Crear la ventana secundaria
    ventana_mensaje = tk.Toplevel()
    ventana_mensaje.title("Escribir Mensaje")
    ventana_mensaje.geometry("1200x800")

    # Instrucciones para el usuario, incluyendo un ejemplo de cómo usar {nombre} y {genero}
    instrucciones = tk.Label(ventana_mensaje, text=(
        "Escribe el mensaje que quieres enviar.\n"
        "Puedes usar las variables {nombre} y {genero} para personalizar los mensajes.\n"
        "Ejemplo: 'Hola {genero} {nombre}, espero que estés bien.'"
    ))
    instrucciones.pack(pady=10)

    # Campo de texto grande para el mensaje
    campo_texto = tk.Text(ventana_mensaje, height=30, width=100)
    campo_texto.pack(pady=10)

    # Botón para confirmar el mensaje
    boton_confirmar = tk.Button(ventana_mensaje, text="Confirmar Mensaje", command=confirmar_mensaje)
    boton_confirmar.pack(pady=10)

    ventana_mensaje.mainloop()
