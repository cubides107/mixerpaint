import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import pyfirmata
import time

# Conectar a Arduino utilizando PyFirmata
board = pyfirmata.Arduino('COM10')  # Reemplaza 'COMX' con el puerto serie correcto


# Configurar pines como salidas o entradas según corresponda
amarillo_pin = board.get_pin('d:9:o')
azul_pin = board.get_pin('d:10:o')
rojo_pin = board.get_pin('d:11:o')
negro_pin = board.get_pin('d:12:o')
blanco_pin = board.get_pin('d:13:o')


# Lista de colores
colores = ["Verde C", "Verde O", "Naranja C", "Naranja O", "Violeta C", "Violeta O", "Turquesa", "Cafe", "Gris C", "Gris O", "Rosado", "Rojo", "Azul", "Amarillo", "Negro", "Blanco"]

color_seleccionado = "Verde C"

# Función para enviar el color seleccionado a Arduino
def enviar_color():
    color_seleccionado = combo.get()
    if color_seleccionado in acciones_por_color:
        acciones_por_color[color_seleccionado]()
    else:
        print(f"Acciones para '{color_seleccionado}' no definidas.")

def execute_bomb(time_pin, progress_bar, pin):
    pin.write(1)
    for i in range(11):
        porcentaje = i * 10
        progress_bar["value"] = porcentaje
        ventana.update()
        time.sleep(time_pin / 10)
    pin.write(0)

def reset_progresabar():
    progress_bar_amarillo["value"] = 0
    progress_bar_negro["value"] = 0
    progress_bar_blanco["value"] = 0
    progress_bar_rojo["value"] = 0
    progress_bar_azul["value"] = 0
    


# Función para ejecutar acciones para cada color
def verde_claro():
    execute_bomb(5,progress_bar_amarillo,amarillo_pin)
    execute_bomb(3,progress_bar_azul,azul_pin)
    execute_bomb(2,progress_bar_blanco,blanco_pin)
    reset_progresabar()

def verde_oscuro():
    execute_bomb(5.5,progress_bar_amarillo,amarillo_pin)
    execute_bomb(3,progress_bar_azul,azul_pin)
    execute_bomb(2,progress_bar_negro,negro_pin)
    reset_progresabar()

def naranja_claro():
    execute_bomb(5.5,progress_bar_amarillo,amarillo_pin)
    execute_bomb(4,progress_bar_rojo,rojo_pin)
    execute_bomb(5,progress_bar_blanco,blanco_pin)
    reset_progresabar()

def naranja_oscuro():
    execute_bomb(4,progress_bar_amarillo,amarillo_pin)
    execute_bomb(6,progress_bar_rojo,rojo_pin)
    reset_progresabar()


def violeta_claro():
    execute_bomb(5,progress_bar_azul,azul_pin)
    execute_bomb(4,progress_bar_rojo,rojo_pin)
    execute_bomb(1,progress_bar_blanco,blanco_pin)
    reset_progresabar()

def violeta_oscuro():
    execute_bomb(7,progress_bar_azul,azul_pin)
    execute_bomb(3,progress_bar_rojo,rojo_pin)
    reset_progresabar()

def turquesa():
   execute_bomb(4,progress_bar_azul,azul_pin)
   execute_bomb(3,progress_bar_amarillo,amarillo_pin)
   execute_bomb(3,progress_bar_blanco,blanco_pin)
   reset_progresabar()

def cafe():
   execute_bomb(5,progress_bar_rojo,rojo_pin)
   execute_bomb(3,progress_bar_amarillo,amarillo_pin)
   execute_bomb(2,azul_pin,azul_pin)
   reset_progresabar()

def gris_claro():
   execute_bomb(8,progress_bar_blanco,blanco_pin)
   execute_bomb(2,progress_bar_negro,negro_pin)
   reset_progresabar()

def gris_oscuro():
   execute_bomb(2,progress_bar_blanco,blanco_pin)
   execute_bomb(8,progress_bar_negro,negro_pin)
   reset_progresabar()

def rosado():
   execute_bomb(3,progress_bar_blanco,blanco_pin)
   execute_bomb(7,progress_bar_rojo,rojo_pin)
   reset_progresabar()

def rojo():
    execute_bomb(10,progress_bar_rojo,rojo_pin)
    reset_progresabar()

def azul():
   execute_bomb(10,progress_bar_azul,azul_pin)
   reset_progresabar()

def amarillo():
   execute_bomb(10,progress_bar_amarillo,amarillo_pin)
   reset_progresabar()

def negro():
    execute_bomb(10,progress_bar_negro,negro_pin)
    reset_progresabar()

def blanco():
    execute_bomb(10,progress_bar_blanco,blanco_pin)
    reset_progresabar()

# Crear un diccionario que mapea colores a funciones
acciones_por_color = {
    "Verde C": verde_claro,
    "Verde O": verde_oscuro,
    "Naranja C": naranja_claro,
    "Naranja O": naranja_oscuro,
    "Violeta C": violeta_claro,
    "Violeta O": violeta_oscuro,
    "Turquesa": turquesa,
    "Cafe": cafe,
    "Gris C": gris_claro,
    "Gris O": gris_oscuro,
    "Rosado": rosado,
    "Rojo": rojo,
    "Azul": azul,
    "Amarillo": amarillo,
    "Negro": negro,
    "Blanco": blanco
}


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Control de Bombas")

# Añade una imagen a la ventana
imagen = PhotoImage(file="C:\\Users\\crist\\Downloads\\arduino\\1.png") 
imagen = imagen.subsample(4)
imagen_label = tk.Label(ventana, image=imagen)
imagen_label.pack(side="right")

# Agrega un título
titulo_label = ttk.Label(ventana, text="Mixer", font=("Arial", 16))
titulo_label.pack(pady=10)

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
style = ttk.Style()
style.theme_use("default")  # Cambia el tema de estilo predeterminado
style.configure("Red.Horizontal.TProgressbar", background='red')
label_rojo = ttk.Label(ventana, text="Rojo:")
label_rojo.pack()
progress_bar_rojo = ttk.Progressbar(ventana, mode="determinate", length=200,style="Red.Horizontal.TProgressbar")
progress_bar_rojo.pack()


style = ttk.Style()
style.theme_use("default")  # Cambia el tema de estilo predeterminado
style.configure("Azul.Horizontal.TProgressbar", background='blue')
label_azul = ttk.Label(ventana, text="Azul")
label_azul.pack()
progress_bar_azul = ttk.Progressbar(ventana, mode="determinate", length=200, style="Azul.Horizontal.TProgressbar")
progress_bar_azul.pack()


style = ttk.Style()
style.theme_use("default")  # Cambia el tema de estilo predeterminado
style.configure("Amarillo.Horizontal.TProgressbar", background='yellow')
label_amarillo = ttk.Label(ventana, text="Amarillo")
label_amarillo.pack()
progress_bar_amarillo = ttk.Progressbar(ventana, mode="determinate", length=200,style="Amarillo.Horizontal.TProgressbar")
progress_bar_amarillo.pack()



style = ttk.Style()
style.theme_use("default")  # Cambia el tema de estilo predeterminado
style.configure("Blanco.Horizontal.TProgressbar", background='white')
label_blanco = ttk.Label(ventana, text="Blanco")
label_blanco.pack()
progress_bar_blanco = ttk.Progressbar(ventana, mode="determinate", length=200, style="Blanco.Horizontal.TProgressbar")
progress_bar_blanco.pack()


style = ttk.Style()
style.theme_use("default")  # Cambia el tema de estilo predeterminado
style.configure("Negro.Horizontal.TProgressbar", background='black')
label_negro = ttk.Label(ventana, text="Negro")
label_negro.pack()
progress_bar_negro = ttk.Progressbar(ventana, mode="determinate", length=200, orient="horizontal",  style="Negro.Horizontal.TProgressbar")
progress_bar_negro.pack()



# Función para cerrar la conexión con Arduino al cerrar la ventana
def cerrar_ventana():
    board.exit()
    ventana.destroy()

ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana)

ventana.mainloop()
