import os



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

