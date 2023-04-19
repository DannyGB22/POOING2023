from tkinter import *
from tkinter import  ttk
import tkinter as tk
from Controlador import *

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

Ventana.mainloop()