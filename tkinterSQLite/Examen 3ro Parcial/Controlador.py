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
            
            
    def guardarUsuario(self,Cnt,Num,Sal,):
        
        #1.- Llamar a la conexion
        conx = self.conexionBD()
        
        #2.- Revisar parametros vacios
        
        if(Cnt == "" or Num == "" or Sal == ""):
            messagebox.showwarning("Aguas", "Revisa tu formulario")
            conx.close()
        else:
            #3.- Preparar datos y el querySQL
            cursor = conx.cursor()
            datos = (Cnt, Num, Sal )
            qrInsert="insert into TBCuentas(IDCuenta,NoCuenta,Saldo) values(?,?,?)"
            
            #4.- Proceder a Insertar y cerramos la base de datos
            cursor.execute(qrInsert,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito", "Se guardo la cuenta existosamente")


    def actualizar(self,ID,Cnt,Num,Sal):
        
        conx = self.conexionBD()
        
        if(ID == "" or Cnt == "" or Num == "" or Sal == ""):
            messagebox.showwarning("Aguas", "Revisa tu formulario")
            conx.close()
        else:
            #Preparar datos y el querySQL
            cursor = conx.cursor()
            datos = (Cnt, Num, Sal, ID)
            qrInsert="update TBCuentas set IDCuenta=?,NoCuenta=?,Saldo=?, where ID=?"
            
            #Proceder a Insertar y cerramos la base de datos
            cursor.execute(qrInsert,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito", "Se actualizo la cuenta exitosamente")

   
    def consulta(self):
        #1.- Preparamos nuestra conexion a base de datos
        

        conx =self.conexionBD()

        try:
            #Preparamos el select
            cursor = conx.cursor()
            sqlSelect = "select * from TBCuentas"
            #Ejecutamos la consulta
            cursor.execute(sqlSelect)
            RSusuario = cursor.fetchall()
            conx.close()
                
            return RSusuario
                
        except sqlite3.OperationalError:
            print("Error en la consulta")