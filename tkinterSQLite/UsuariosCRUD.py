from tkinter import *
from tkinter import ttk
import tkinter as tk



ventana = Tk()
ventana.title("CRUD Usuarios ")
ventana.geometry("500x300")



panel = ttk.Notebook(ventana)
panel.pack(fill="both", expand="yes")

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)


#pastana1: formulario Usuarios 

titulo= Label(pestana1, text="Registro de usuarios", fg="Blue", font=("modern", 18)).pack()


varNom= tk.StringVar()
LblNom= Label(pestana1, text="Nombre: ").pack()
txtNom= Entry(pestana1, textvariable=varNom).pack()

varCor= tk.StringVar()
LblCor= Label(pestana1, text="Correo: ").pack()
txtCor= Entry(pestana1, textvariable=varCor).pack()

varCon= tk.StringVar()
LblCon= Label(pestana1, text="Contraseña: ").pack()
txtCon= Entry(pestana1, textvariable=varCon).pack()

panel.add(pestana1, text="Formulario de ussuarios ")
panel.add(pestana2, text="Buascar Usuario ")
panel.add(pestana3, text="Consultar Usuario ")
panel.add(pestana4, text="Actualizar Usuario ")

btnGuardar= Button(pestana1, text="Guardar Uauario").pack()

ventana.mainloop()