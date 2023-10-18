import tkinter as tk
from tkinter import ttk
import pyfirmata
import time

# Conectar a Arduino utilizando PyFirmata
board = pyfirmata.Arduino('COM10')  # Reemplaza 'COMX' con el puerto serie correcto

# Configurar pines como salidas o entradas según corresponda
pines = {
    "rojo": board.get_pin('d:11:o'),
    "azul": board.get_pin('d:10:o'),
    "amarillo": board.get_pin('d:9:o'),
    "blanco": board.get_pin('d:13:o'),
    "negro": board.get_pin('d:12:o')
}

# Lista de colores
colores = ["Rojo", "Azul", "Amarillo", "Blanco", "Negro"]

# Función para enviar el color seleccionado a Arduino
def enviar_color():
    color_seleccionado = combo.get()
    if color_seleccionado in pines:
        acciones_por_color[color_seleccionado]()
    else:
        print(f"Acciones para '{color_seleccionado}' no definidas.")

# Función para ejecutar acciones para cada color
def activar_pin(pin, barra, tiempo_espera):
    pin.write(1)
    for i in range(11):
        porcentaje = i * 10
        barra["value"] = porcentaje
        ventana.update()
        time.sleep(tiempo_espera / 10)
    pin.write(0)

def rojo():
    print("Seleccionaste el color: Rojo")
    print("Creando Color Rojo")
    activar_pin(pines["rojo"], progress_bar_rojo, 5)

def azul():
    print("Seleccionaste el color: Azul")
    print("Creando Color Azul")
    activar_pin(pines["azul"], progress_bar_azul, 3)

def amarillo():
    print("Seleccionaste el color: Amarillo")
    print("Creando Color Amarillo")
    activar_pin(pines["amarillo"], progress_bar_amarillo, 5)

def blanco():
    print("Seleccionaste el color: Blanco")
    print("Creando Color Blanco")
    activar_pin(pines["blanco"], progress_bar_blanco, 2)

def negro():
    print("Seleccionaste el color: Negro")
    print("Creando Color Negro")
    activar_pin(pines["negro"], progress_bar_negro, 5)

# Crear un diccionario que mapea colores a funciones
acciones_por_color = {
    "Rojo": rojo,
    "Azul": azul,
    "Amarillo": amarillo,
    "Blanco": blanco,
    "Negro": negro
}

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Control de Bombas")

# Aplica el tema "elegance" al estilo de la interfaz
style = ttk.themes.ThemedStyle(ventana)
style.set_theme("elegance")

# Etiqueta
label = ttk.Label(ventana, text="Selecciona un color:")
label.pack(pady=10)

# Cuadro combinado (ComboBox) para seleccionar el color
combo = ttk.Combobox(ventana, values=colores)
combo.pack(pady=10)
combo.set(colores[0])

# Botón para enviar el color seleccionado a Arduino
enviar_button = ttk.Button(ventana, text="Enviar Color", command=enviar_color)
enviar_button.pack(pady=10)

# Barras de progreso para cada color
progress_bar_rojo = ttk.Progressbar(ventana, mode="determinate", length=200)
progress_bar_rojo.pack()
label_rojo = ttk.Label(ventana, text="Rojo")
label_rojo.pack()

progress_bar_azul = ttk.Progressbar(ventana, mode="determinate", length=200)
progress_bar_azul.pack()
label_azul = ttk.Label(ventana, text="Azul")
label_azul.pack()

progress_bar_amarillo = ttk.Progressbar(ventana, mode="determinate", length=200)
progress_bar_amarillo.pack()
label_amarillo = ttk.Label(ventana, text="Amarillo")
label_amarillo.pack()

progress_bar_blanco = ttk.Progressbar(ventana, mode="determinate", length=200)
progress_bar_blanco.pack()
label_blanco = ttk.Label(ventana, text="Blanco")
label_blanco.pack()

progress_bar_negro = ttk.Progressbar(ventana, mode="determinate", length=200)
progress_bar_negro.pack()
label_negro = ttk.Label(ventana, text="Negro")
label_negro.pack()

# Función para cerrar la conexión con Arduino al cerrar la ventana
def cerrar_ventana():
    board.exit()
    ventana.destroy()

ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana)

ventana.mainloop()
