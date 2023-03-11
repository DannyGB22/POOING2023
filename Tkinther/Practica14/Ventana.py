import tkinter as tk

class VentanaPrincipal:
    def interfaz(self):
        #self.caja_popular = caja_popular

        ventana = tk.Tk()
        ventana.title("Caja Popular")

        # Crear widgets de la interfaz
        label_titulo = tk.Label(ventana, text="Administración de cuenta en Caja Popular")
        label_titulo.pack(pady=10)

        frame_datos_cuenta = tk.Frame(ventana)
        frame_datos_cuenta.pack()

        label_num_cuenta = tk.Label(frame_datos_cuenta, text="No. Cuenta:")
        label_num_cuenta.grid(row=0, column=0, padx=5, pady=5)
        entry_num_cuenta = tk.Entry(frame_datos_cuenta)
        entry_num_cuenta.grid(row=0, column=1, padx=5, pady=5)

        label_titular = tk.Label(frame_datos_cuenta, text="Titular:")
        label_titular.grid(row=1, column=0, padx=5, pady=5)
        entry_titular = tk.Entry(frame_datos_cuenta)
        entry_titular.grid(row=1, column=1, padx=5, pady=5)

        label_edad = tk.Label(frame_datos_cuenta, text="Edad:")
        label_edad.grid(row=2, column=0, padx=5, pady=5)
        entry_edad = tk.Entry(frame_datos_cuenta)
        entry_edad.grid(row=2, column=1, padx=5, pady=5)

        label_saldo = tk.Label(frame_datos_cuenta, text="Saldo:")
        label_saldo.grid(row=3, column=0, padx=5, pady=5)
        entry_saldo = tk.Entry(frame_datos_cuenta)
        entry_saldo.grid(row=3, column=1, padx=5, pady=5)

        button_agregar_cuenta = tk.Button(ventana, text="Agregar Cuenta", command= agregar_cuenta)
        button_agregar_cuenta.pack()
        
        ventana.mainloop()
        
        
        
        