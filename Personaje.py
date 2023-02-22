class Personaje:
   
   #definimos el constructor del personaje
   def __init__(self,esp,nom,alt):
    
    
    #Atributos Personajes
    self.Especie= esp
    self.Nombre = nom
    self.Altura = alt
    
    
#Metodos del personaje
def Correr(self,status):
    if(status):
        print("El personaje "+self.Nombre+ "esta corriendo")
    else:
        print("El personaje "+self.Nombre + "se detuvo")

    
def lanzarGranadas(self):
    print("El personaje"+ self.nombre+ "lanzo una granada")
    
    
def recargarArma(self, municiones):
    cargador=10
    cargador= cargador + municiones
    print("El arma tiene"+ str(cargador) +"balas")
   