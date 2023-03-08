from tkinter import *
import tkinter as tk
import tkinter.messagebox as messagebox

class PasswordGenerator:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Generador de contraseñas")
        self.ventana.geometry("400x200")

        self.length_var = tk.IntVar()
        self.length_var.set(8)
        self.uppercase_var = tk.BooleanVar()
        self.special_chars_var = tk.BooleanVar()

        tk.Label(self.ventana, text="Longitud de la contraseña:").pack()
        tk.Entry(self.ventana, textvariable=self.length_var).pack()

        tk.Checkbutton(self.ventana, text="Incluir mayúsculas", variable=self.uppercase_var).pack()
        tk.Checkbutton(self.ventana, text="Incluir caracteres especiales", variable=self.special_chars_var).pack()

        tk.Button(self.ventana, text="Generar contraseña", command=self.generate_password).pack()
        tk.Button(self.ventana, text="Comprobar fortaleza", command=self.check_strength).pack()
