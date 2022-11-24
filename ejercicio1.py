import os
mensajes = {"A" : 0.2, "F" : 0.17, 1 : 0.13, 3: 0.21, 0: 0.05, "M": 0.09, "T": 0.15 }

#class Nodo: 
 #   def __init__(self, value = None): 
  #      self.value = value
   #     self.left = None
  #      self.right = None
    
#    def set_valor(self, value):
      #  self.value = value

   # def get_valor(self):
    #      return self.value
    
   # def nodo_hijo_izq(self, left):
   #     self.left = left
   #     return self.left
    
   # def nodo_hijo_der(self, right):
    #    self.right = right
   #     return self.right

  #  def hueco_izq(self):
    #    return self.left != None
    
   # def hueco_der(self):
      #  return self.right != None
    

class Nodo:
    probabilidad = 0.0
    simbolo = ""
    codificacion = ""
    visited = False
    longitud = -1

class Huffman:
    tree = None 
    root = None
    nodos = []
    prob = {}
    dicEncoder ={}

    def __init__(self, simbolo):
        self.simbolo = simbolo
        self.construir_arbol()
        self.construir_dict()

    def construir_nodos(self,prob):
        for simbolo in prob:
            nodo = Nodo()
            nodo.simbolo = simbolo
            nodo.probabilidad = prob[simbolo]
            nodo.visited = False
            self.nodos.append(nodo)
            self.prob[simbolo] = prob[simbolo]

    def construir_arbol(self):