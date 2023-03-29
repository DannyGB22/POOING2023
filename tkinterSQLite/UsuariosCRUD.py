from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

from ControladorBD import * # Le presentamos la clase a la ventana 

# Crear una objeto de tipo controlador
controlador = controladorBD()

# Proceder a guardar el metodo del objeto del contolador 

def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(), varCor.get(), varCon.get())
 
 
def ejecutaSelectU():
    rsUsuario = controlador.consultaUsuario(varBus.get())
    
    for usu in rsUsuario:
        cadena = str(usu[0])+" "+ usu[1]+" "+ usu[2]+" "+ str(usu[3])
    
    
    if(rsUsuario): 
        
        print(cadena)
    else:
        messagebox.showinfo("No encontrado", "usuario no registrado en la BD")
        


 
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
panel.add(pestana2, text="Buscar Usuario ")
panel.add(pestana3, text="Consultar Usuario ")
panel.add(pestana4, text="Actualizar Usuario ")

btnGuardar= Button(pestana1, text="Guardar Usuario",command=ejecutaInsert).pack()

#Pesataña 2; Buscar Usuario 

titulo2= Label(pestana1, text="Buscar Usuario", fg="green", font=("modern", 18)).pack()


varBus= tk.StringVar()
Lblid= Label(pestana2, text="Identificador de usuario: ").pack()
txtid= Entry(pestana2, textvariable=varBus).pack()
btnBusqueda=Button(pestana2,text="Buscar", command= ejecutaSelectU).pack()

subBus= Label(pestana2, text="Registrado:", fg= "blue", font=("Modern", 15) ).pack()
texBus=tk.Text(pestana2, height=5, width=52).pack()



ventana.mainloop()

