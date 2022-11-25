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
while len(nodos)>1:
    izquierda=heapq.heappop(nodos)
    derecha= heapq.heappop(nodos)
    izquierda.huff =0
    derecha.huff = 1
    nuevo_nodo= Nodo(izquierda.p+derecha.p, izquierda.simbolos + derecha.simbolos, izquierda, derecha)
    heapq.heappush(nodos, nuevo_nodo)

print(Nodo(nodos[0]))
