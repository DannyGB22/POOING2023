from tkinter import messagebox

class Validador2:
    
    def __init__(self):
        self.__Activo = True

    def validarDatos(self,correo, contrasena):
        
        if not correo or not contrasena:
            messagebox.showerror("Error", "Correo o contraseña vacíos.")
        elif correo == "danny22@gmail.com" and contrasena == "danny2022":
            messagebox.showinfo("Bienvenido", "Bienvenido, {}.".format(correo))
        else:
            messagebox.showerror("Error", "Revise sus datos.")
        