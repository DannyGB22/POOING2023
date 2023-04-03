from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from tkinter.messagebox import showinfo

from ControladorBD import * # Le presentamos la clase a la ventana 

# Crear una objeto de tipo controlador
controlador = controladorBD()

# Proceder a guardar el metodo del objeto del contolador
 
#pestana1
def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(), varCor.get(), varCon.get())

 
#pestana2 
def ejecutaSelectU():
    #Obtener el valor del campo de busqueda del id y validar que no este vacio
    id_obtenido = varBus.get()
    if (id_obtenido == ""):
        messagebox.showwarning("Valor vacio", "Revisa tu formulario")
        return

    #Llamar al metodo de consulta y se le pasa el id
    rsUsuario = controlador.consultaUsuario(id_obtenido)

    #Limpiar el campo de texto (Para que no se acumulen los resultados)
    texBus.delete(1.0, tk.END)

    #Iterar el resultado de la consulta
    #contador = 1
    for resultado in rsUsuario:
        #Solo muestra Id, nombre y correo
        mensaje = "ID: " + str(resultado[0]) + "\n" + "NOMBRE: " + str(resultado[1]) + "\n" + "EMAIL: " + str(
            resultado[2]) + "\n" + "\n"
        #contador += 1
        texBus.insert(tk.END, "\n" + mensaje)
    if (rsUsuario):
        pass
        #print(mensaje)
    else:
        messagebox.showinfo("No encontrado", "usuario no registrado en la BD")

        
#pestana3
def ejecutaConsultas():
    Usus= controlador.cosultarUsus()
    
    for i in tree.get_children():
        tree.delete(i)
        
        
    for usu in Usus:
        tree.insert("", END, values=(usu[0], usu[1], usu[2], usu[3]))
        

 
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

titulo2= Label(pestana2, text="Buscar Usuario", fg="green", font=("modern", 18)).pack()


varBus= tk.StringVar()
Lblid= Label(pestana2, text="Identificador de usuario: ").pack()
txtid= Entry(pestana2, textvariable=varBus).pack()
btnBusqueda=Button(pestana2,text="Buscar", command= ejecutaSelectU).pack()

subBus= Label(pestana2, text="Registrado:", fg= "blue", font=("Modern", 15) ).pack()
texBus=tk.Text(pestana2, height=5, width=52).pack()



#pestaña 3 consultar usuarios

titulo3 = Label(pestana3, text="Consultar Usuarios", fg="red", font=("modern", 18)).pack()

columnas = ('id', 'nombre', 'correo', 'contra')

tree = ttk.Treeview(pestana3, columns= columnas, show='headings')

# se definen los headings
tree.heading('id', text='ID')
tree.heading('nombre', text='Nombre')
tree.heading('correo', text='Email')
tree.heading('contra', text='Contraseña')
tree.pack()

btnconsulta= Button(pestana3, text="consultar", command= ejecutaConsultas)
btnconsulta.pack()



ventana.mainloop()

