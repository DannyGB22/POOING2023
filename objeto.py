from Personaje import *
#1. solicitar Datos
print("")
print("#####Datos Heroe#")
especieH = input("Escribe la especie del Heroe: ")
nombreH = input("Escribe el nombre del Heroe: ")
alturaH= float(input("Escribe la altura del Heroe: "))
recargaH = int(input("Cauntas balas recargas al Heroe: "))

print("")
print("#####Datos Villano#")
especieV = input("Escribe la especie del Villano: ")
nombreV = input("Escribe el nombre del Villano: ")
alturaV = float(input("Escribe la altura del Villano: "))
recargaV = int(input("Cauntas balas recargas al Villano: "))


#2. Crear los Objetos del personaje

heroe= Personaje(especieH,nombreH,alturaH)
villano= Personaje(especieV,nombreV,alturaV)

#3. usar los atributos

#Ejemolo de set para un atributo
heroe.setNombre("Pepe pecas")

print("")
print("#####Objeto Heroe#")
print("El personaje se llama:"+heroe.getNombre())
print("Pertenece a la especie: "+heroe.getEspecie())
print("Y tiene una altura de"+str(heroe.getAltura()))

#4. Usar metodos
heroe.Correr(True)
heroe.lanzarGranadas()
heroe.recargarArma(recargaH)

#Ejemplo de un metodo privado
#heroe.__pensar()

#3. usar los atributos
print("")
print("#####Objeto Villano#")
print("El personaje se llama:"+villano.getNombre())
print("Pertenece a la especie: "+villano.getEspecie())
print("Y tiene una altura de"+str(villano.getAltura()))

#3. Usar metodos
villano.Correr(False)
villano.lanzarGranadas()
villano.recargarArma(recargaV)