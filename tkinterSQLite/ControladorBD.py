from tkinter import messagebox
import sqlite3
import bcrypt 

class controladorBD: 
    
    def __init__(self):
        pass
    
   
    #1 preparamos la conexion para usarla cuando sea necesario
    def conexionBD(self):
         
        try:
            conexion=sqlite3.connect("C:/Users/NextClick/OneDrive/Documentos/POOING2023/tkinterSQLite/DatabaseUsuarios.db")
            print("conectado a la base de datos ")
            return conexion
       
        except sqlite3.OperationalError:
             print("No se pudo conectar")
            
            
            
            
    def guardarUsuario(self, nom, cor,con):
     
     
     #1. llamar a la conexion 
       conx= self.conexionBD()
     
     
     
     #2. revisar parametros vacio
       if(nom==""or cor==""or con==""):
           messagebox.showwarning("Agua!!", "Revisa tu formulario")
           conx.close()
       else:
           #3. preparar los datos y el querysql
           cursor=conx.cursor()
           conH=self.encriptarCon(con)
           datos=(nom,cor,conH)
           qrInsert="insert into TB_registrados(nombre,correo,contra) values(?,?,?)"
        
           #4. Proceder a insertar y cerramaos la conex
           cursor.execute(qrInsert,datos)
           conx.commit()
           conx.close()
           messagebox.showinfo("Exito", "Se guardo el usuario")
           
            
    
    def encriptarCon(self,con):
        conPlana= con
        conPlana= conPlana.encode() #convertimos la contra a bytes
        sal= bcrypt.gensalt()
        conHa=bcrypt.hashpw(conPlana, sal)
        print(conHa)  
        return conHa         
     
      
     
     
