from tkinter import messagebox
import sqlite3

class controladorBD_Banco:
    
    def __init__(self):
        pass
    #Preparamos la conexion a la base de datos para usarla cuando se ocupe
    def conexionBD(self):
        try:
            conexion = sqlite3.connect("BD_Banco.db")
            print("Conexion exitosa")
            return conexion
        
        except sqlite3.OperationalError:
            print("No se pudo conectar")