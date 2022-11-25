import csv
import numpy as np
import pandas as pd

f = open("pokemon.csv")
reader = csv.reader(f)
l = list(reader)
nombres = []
for i in range(1, len(l)):
    nombres.append(l[i][1]) # con esto creamos una lista para los nombres de los pokemons

bul1= list(filter(lambda x: "Bul" in x, nombres))
bul2 = list(filter(lambda x: "bul" in x, nombres))
bul = bul1 + bul2


#Tipos de pokemons:

tipos = []
for i in range(1, len(l)):
    tipos.append(l[i][2])

fire = list(filter(lambda x: "Fire" in x, tipos))
water = list(filter(lambda x: "Water" in x, tipos))
grass = list(filter(lambda x: "Grass" in x, tipos))
bug = list(filter(lambda x: "Bug" in x, tipos))




class Nodo:
    def __init__(self,dato):
        self.dato = dato 
        self.izquierda = None 
        self.derecha = None 

    def agregar_recursivo(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self.agregar_recursivo(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.agregar_recursivo(nodo.derecha, dato)
    
    def inorder_recursivo(self, nodo):
        if nodo is not None:
            self.inorder_recursivo(nodo.izquierda)
            print(nodo.dato, end=",")
            self.inorder_recursivo(nodo.derecha)

    def preorden_recursivo(self,nodo):
        if nodo is not None:
            print(nodo.dato, end=",")
            self.preorden_recursivo(nodo.izquierda)
            self.preorden_recursivo(nodo.derecha)
    
    def buscar(self, nodo, busqueda):
        if nodo is None:
            return None 
        if nodo.dato == busqueda:
            return nodo
        if busqueda < nodo.dato:
            return self.buscar(nodo.izquierda, busqueda)
        else:
            return self.buscar(nodo.derecha, busqueda)
    
    def agregar(self, dato):
        self.agregar_recursivo(self.raiz, dato)
    
    def inorden(self):
        print("Imprimiendo árbol...")
        self.inorder_recursivo(self.raiz)
        print("")

    def preorden(self):
        print("Imprimiendo árbol preorden...")
        self.preorden_recursivo(self.raiz)
        print("")
    
    def postorden(self):
        print("Imprimiendo árbol postorden...")
        self.postorden_recursivo(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self.buscar(self.raiz, busqueda)
