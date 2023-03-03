from tkinter import *
from tkinter import messagebox
#import Validador
from Validador2 import *

def sendData():
    correo = entry_correo.get()
    contrasena = entry_contrasena.get()
    Validador.validarDatos(correo, contrasena)

Validador = Validador2()
ventana = Tk()
ventana.geometry("600x400")
ventana.title("Interfaz de login")


etiqueta = Label(ventana, text="LOGIN")
etiqueta.pack()

correo = Label(ventana, text="Correo:")
correo.pack()
entry_correo = Entry(ventana)
entry_correo.pack()

contrasena = Label(ventana, text="Contraseña:")
contrasena.pack()
entry_contrasena = Entry(ventana, show="*")
entry_contrasena.pack()

#correo = entry_correo.get()
#contrasena = entry_contrasena.get()
           
        
boton_iniciar_sesion = Button(ventana, text="Iniciar sesión", command=sendData)
boton_iniciar_sesion.pack()

            
ventana.mainloop()



