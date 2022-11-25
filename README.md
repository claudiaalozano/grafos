# grafos
Mi dirección de GitHub es: https://github.com/claudiaalozano/grafos.git
En este trabajo he realizado elcódigo para áboles binarios, de huffman y grafos. La tarea se dividía en tres ejercicios.

### Ejercicio 1
```
import os
import heapq


class Nodo:
    def __init__(self,frequencia,simbolo,izquierda = None,derecha=None):
        self.frequencia = frequencia
        self.simbolo = simbolo
        self.izquierda = izquierda
        self.derecha = derecha
        self.huff = ""
    
    def freq(self,nxt):
        return self.frequencia< nxt.frequencia

def dibujar_los_nodos(Nodo, val=""):
    nv= val + str(Nodo.huff)

    if (Nodo.izquierda):
        dibujar_los_nodos(Nodo.izquierda,nv)
    if (Nodo.derecha):
        dibujar_los_nodos(Nodo.derecha)
    if (not Nodo.izquierda and not Nodo.derecha):
        print (f"{Nodo.simbolo} y su nuevo valor es {nv}")


simbolos = ["A", "F", 1 , 3 , 0, "M", "T"]

p = [0.2, 0.17, 0.13, 0.21, 0.05, 0.09, 0.15]

nodos = []

for x in range(len(simbolos)):
    heapq.heappush(nodos, Nodo(p[x], simbolos[x]))

while len(nodos) > 1:
    izquierda=heapq.heappop(nodos)
    derecha= heapq.heappop(nodos)
    izquierda.huff =0
    derecha.huff = 1
    nuevo_nodo= Nodo(izquierda.p+derecha.p, izquierda.simbolos + derecha.simbolos, izquierda, derecha)
    heapq.heappush(nodos, nuevo_nodo)

```

### Ejercicio 2
```
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
```


### Ejercicio 3

```
import pandas as pd
import networkx as nx
import numpy as np

data = {"Nombre":["Petra","Taj Mahal", "Machu Picchu", "Pirámide de Chichén Itzá", "Coliseo de Roma", "Gran Muralla China", "Cristo Redentor"], "Ubicación":["Jordania", "India", "Perú", "Yucatán", "Roma", " China", "Brasil"], "Tipo":["Arquitectura", "Arquitectura", "Arquitectura", "Arquitectura", "Arquitectura", "Arquitectura", "Arquitectura"]}
df = pd.DataFrame(data, columns=['Nombre', "Ubicación", "Tipo"])
df.to_csv("siete_maravillas", index=False)

class Graph:
    def __init__(self,vertex):
        self.vertex = vertex
        self.graph = [[0]* vertex for i in range(vertex)]
    
    def add_edge(self, u, v):
        self.graph[u-1][v-1]=1
        self.graph[v-1][u-1]=1
    
    def show(self):
        for i in self.graph:
            for j in i:
                print(j, end=" ")
            print(" ")

g = Graph(data)

```
