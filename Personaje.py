class Personaje:
   
   #definimos el constructor del personaje
   def __init__(self,esp,nom,alt):
    
    
    #Definimos el constructor de personaje y los encapsulamos
       self.__Especie= esp
       self.__Nombre = nom
       self.__Altura = alt
    
    
    #Metodos del personaje
   def Correr(self,status):
        if(status):
            print("El personaje "+self.__Nombre+ "esta corriendo")
        else:
            print("El personaje "+self.__Nombre + "se detuvo")

    
   def lanzarGranadas(self):
        print("El personaje"+ self.__Nombre+ "lanzo una granada")
            
            
   def recargarArma(self, municiones):
        cargador=10
        cargador= cargador + municiones
        print("El arma tiene "+ str(cargador) +" balas")
    
   def pensar(self):
        print("Estoy pensando ")
        
    
   
    #Declarar Getters & setters de atributos

   def getNombre(self):
        return self.__Nombre

   def setNombre(self, nom):
        self.__Nombre=nom
            
            
   def getEspecie(self):
        return self.__Especie

   def setEspecie(self, esp):
        self.__Especie=esp
            
        
   def getAltura(self):
        return self.__Altura

   def setAltura(self, alt):
        self.__Altura=alt
            
        
        