from Personaje import *
#1. solicitar Datos
print("")
print("#####Datos Heroe#")
especieH = input("Escribe la especie del Heroe: ")
nombreH = input("Escribe el nombre del Heroe: ")
alturaH= float(input("Escribe la altura del Heroe"))
recargaH = int(input("Cauntas bals recargas al Heroe: "))

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
print("")
print("#####Objeto Heroe#")
especieH = input("El personaje se llama:"+heroe.Nombre)
nombreH = input("Pertenece a la especie: "+heroe.Especie)
alturaH= float(input("Y tiene una altura de"+str(heroe.Altura)))

#4. Usar metodos
heroe.Correra(True)
heroe.lanzarGranadas()
heroe.recargarArma(recargaH)

#3. usar los atributos
print("")
print("#####Objeto Villano#")
especieV = input("El personaje se llama:"+villano.Nombre)
nombreV = input("Pertenece a la especie: "+villano.Especie)
alturaV= float(input("Y tiene una altura de"+str(villano.Altura)))

#3. Usar metodos
villano.Correra(False)
villano.lanzarGranadas()
villano.recargarArma(recargaV)