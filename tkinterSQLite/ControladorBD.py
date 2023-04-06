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
  
    
    def consultaUsuario(self, id):
        #1. Prepararla conexion
        conx= self.conexionBD()
     
        #2. verificar que el ID no este vacio 
     
        if(id == ""):
         messagebox.showwarning("Cuidado", "ID vacio escribe uno valido")
         conx.close() 
        else:
         #3. proceder a buscar
            try:
                #4. preparar o necesario para el select
                cursor= conx.cursor()
                sqlSelect= "select * from TB_registrados where id=  "+id
                
                #5. Ejecucion y guardado de la consulta
                cursor.execute(sqlSelect)
                RSusuario=cursor.fetchall()
                conx.close()
                
                return RSusuario
                
                
            except sqlite3.OperationalError:
                print("Errror consulta")
             
    
  
    def cosultarUsus(self):
        conx= self.conexionBD()
        
        try:
            cursor= conx.cursor()
            sqlSelect= "select id, nombre, correo, contra FROM TB_registrados"
            
            cursor.execute(sqlSelect)
            RSusuario=cursor.fetchall()
            conx.close()
                
             
            return RSusuario
                
        except sqlite3.OperationalError:
            print("Error de consulta")
            
    
   
   
    def actualizarUsuario(self, id, nombre, correo, contra):
        # Buscar usuario en la base de datos por su id y actualizarlo
        if (id == "" and correo == "" and contra == "" and nombre == ""):
            messagebox.showwarning("CUIDADO", "Todos los campos estan vacios")
            return
        elif (id == "" or correo == "" or contra == "" or nombre == ""):
            messagebox.showwarning("CUIDADO", "Revisa tus datos, uno o mas campos estan vacios")
            return

    
        conx = self.conexionBD()
        cursor = conx.cursor()
        contra= self.encriptarCon(contra)
        # Si el usuario existe se intenta actualizar
        try:
            cursor.execute("UPDATE TB_registrados SET nombre = ?, correo = ?, contra = ? WHERE id = ?", (nombre, correo, contra, id))
            conx.commit()
            conx.close()
            messagebox.showinfo("EXITO", "Se actualizo el usuario")
        # Si ocurre un error al consultar el usuario se muestra un mensaje de error
        except sqlite3.OperationalError:
            messagebox.showwarning("Error", "Ocurrio un error al actualizar el usuario")                       
            
            

    def eliminarUsuario(self, id):
        # Buscar usuario en la base de datos por su id y eliminarlo
        if (id == ""):
            messagebox.showwarning("CUIDADO", "El campo id esta vacio")
            return


        conx = self.conexionBD()
        cursor = conx.cursor()
        
        # Si el usuario existe se intenta eliminar
        try:
            cursor.execute("DELETE FROM TB_registrados WHERE id = ?", (id,))
            conx.commit()
            conx.close()
            messagebox.showinfo("EXITO", "Se elimino el usuario")
        # Si ocurre un error al consultar el usuario se muestra un mensaje de error
        except sqlite3.OperationalError:
            messagebox.showwarning("Error", "Ocurrio un error al eliminar el usuario")
            
            
            