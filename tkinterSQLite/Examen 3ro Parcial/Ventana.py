from tkinter import *
from tkinter import  ttk
import tkinter as tk
from Controlador import *

controlador = controladorBD_Banco

Ventana= Tk()
Ventana.title("BANCO BBVA")
Ventana.geometry("700x500")


panel = ttk.Notebook(Ventana)
panel.pack(fill="both",expand="yes")

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)


#Estilo personalizado para cada pestaña
style1 = ttk.Style()
style1.configure('Custom1.TFrame', background='lightblue')

style2 = ttk.Style()
style2.configure('Custom2.TFrame', background='lightgreen')

style3 = ttk.Style()
style3.configure('Custom3.TFrame', background='yellow')

# Estilo personalizado apropiado a cada pestaña
pestana1.configure(style='Custom1.TFrame')
pestana2.configure(style='Custom2.TFrame')
pestana3.configure(style='Custom3.TFrame')

#Registro de cuentas 

titulo = Label(pestana1,text="Registro de Cuenta", bg="black", fg="white", font=("Times",18)).pack(pady=8)

varCnt = tk.StringVar()
lblCnt = Label(pestana1, text="ID Cuenta: ", font=("Times",10), bg="#E5D835").pack(pady=10)
txtCnt = Entry(pestana1,textvariable=varCnt, width=60).pack()

varNum = tk.StringVar()
lblDNum = Label(pestana1, text="Numero de Cuenta: ", font=("Times",10), bg="#E5D835").pack(pady=10)
txtNum = Entry(pestana1,textvariable=varNum, width=60).pack()

varSal = tk.StringVar()
lblSal = Label(pestana1, text="Saldo", font=("Times",10), bg="#E5D835").pack(pady=10)
txtSal = Entry(pestana1,textvariable=varSal, width=60).pack()

btnGuardar = Button(pestana1, text="Guardar Cuenta ", bg="#003E68", fg="white", font=("Arial Black",10), command=ejecutaInsert).pack(pady=18)


#Consulta de todas las cuentas 

Titulo = Label(pestana3,text="Cuentas:",fg="white",font=("Times",18), bg="black").pack(pady=10)
tree = ttk.Treeview(pestana3)
tree['columns']=('IDCuenta', 'NoCuenta', 'Saldo')
tree.column('#0', width=30, minwidth=30)
tree.column('IDCuenta')
tree.column('NoCuenta')
tree.column('Saldo')
tree.heading('#0', text='ID')
tree.heading('IDCuenta', text='Nomero de ID')
tree.heading('NoCuenta', text='Numero de Cuenta')
tree.heading('Saldo', text='Saldo ')
tree.pack(padx=10, pady=10, fill=BOTH, expand=True)
btnBusquedas = Button(pestana3,text="Consultar", bg="blue", fg="white", font=("Arial Black", 10), command=tareas).pack(pady=15)

#Actualizar datos de la cuenta

titulo = Label(pestana2,text="Actualizar Cuentas", fg="white", font=("Times",18), bg="black").pack(pady=10)

BusT4 = tk.StringVar()

lblid= Label(pestana2, text="Numero de tarea: ", bg="#2AEA1E", font=("Times",12)).pack(pady=10)

txtid = Entry(pestana2,textvariable=BusT4, width=60).pack()

varCnt2 = tk.StringVar()

lblCnt = Label(pestana2, text="Nombre: ",bg="#2AEA1E", font=("Times",12)).pack(pady=10)

txtCnt = Entry(pestana2,textvariable=varCnt2, width=60).pack()

varNum2 = tk.StringVar()

lblNum = Label(pestana2, text="Descripcion: ", bg="#2AEA1E", font=("Times",12)).pack(pady=10)

txtNum = Entry(pestana2,textvariable=varNum2, width=60).pack()

varSal2 = tk.StringVar()

lblSal = Label(pestana2, text="Fecha Inicio: ", bg="#2AEA1E", font=("Times",12)).pack(pady=10)

txtSal = Entry(pestana2,textvariable=varSal2, width=60).pack()



btnBusqueda = Button(pestana2,text="Actualizar",command=ejecutaUpdate, bg="#26C6D1", font=("Arial Black", 10), fg="white").pack(pady=15)



panel.add(pestana1, text="Registro de Cuentas")
panel.add(pestana2, text="Actualizar Cuentas")
panel.add(pestana3, text="Consultar")


Ventana.mainloop()
