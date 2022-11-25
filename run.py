from ejercicio2 import *
from ejercicio3 import *
from ejercicio1 import *

if __name__ == '__main__':
    ejercicio = int(input("Introduzca el ejercicio que desea ejecutar: "))

    if ejercicio == 2:
        print("A continuación lista con todos los nombres de los pokemons: ", nombres)
        print("Los pokemons bul son:" , bul)
        t = input("Contador de tipos de pokemons(Fire, Water, Grass o Bug ): ")
        if t == "Fire":
            def counts(fire):
                count = 0
                for i in fire:
                    count += 1
                return count
            print("Contador de pokemons de fuego: ", counts(fire))
        
        elif t == "Water":
            def counts(water):
                count = 0
                for i in water:
                    count += 1
                return count
            print("Contador de pokemons de agua: ", counts(water))
        
        elif t == "Grass":
            def counts(grass):
                    count = 0
                    for i in grass:
                        count += 1
                    return count
            print("Contador de pokemons de planta: ", counts(grass))

        elif t == "Bug":
            def counts(bug):
                count = 0
                for i in bug:
                    count += 1
                return count
            print("Contador de pokemons de insecto: ", counts(bug))
