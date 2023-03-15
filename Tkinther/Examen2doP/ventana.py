from tkinter import *
from datetime import *
import tkinter as tk

class MatriculaApp:
    def __init__(ventana):
        ventana = ventana
       ventana.title("Generador de Matrículas")
        
        # Crear y posicionar los widgets
        tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
        nombre_entry = tk.Entry(ventana)
        nombre_entry.grid(row=0, column=1)
        
        tk.Label(ventana, text="Apellido Paterno:").grid(row=1, column=0)
        apellido_paterno_entry = tk.Entry(ventana)
        apellido_paterno_entry.grid(row=1, column=1)
        
        tk.Label(ventana, text="Apellido Materno:").grid(row=2, column=0)
        apellido_materno_entry = tk.Entry(ventana)
        apellido_materno_entry.grid(row=2, column=1)
        
        tk.Label(ventana, text="Año de nacimiento:").grid(row=3, column=0)
        anio_nacimiento_entry = tk.Entry(ventana)
        anio_nacimiento_entry.grid(row=3, column=1)
        
        tk.Label(ventana, text="Carrera:").grid(row=4, column=0)
        carrera_entry = tk.Entry(ventana)
        carrera_entry.grid(row=4, column=1)
        
    ventana.mainloop()



 


