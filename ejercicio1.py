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
        ind_min1 = self.get_Nodo_minp()
        ind_min2 = self.get_Nodo_minp()

        while ind_min1!= -1 and ind_min2!= -1:
            nodo = Nodo()
            nodo.simbolo = "."
            nodo.codificacion = ""

            prob1 = self.nodos[ind_min1].probabilidad
            prob2 = self.nodos[ind_min2].probabilidad
            nodo.probabilidad = prob1 + prob2
            nodo.visited = False
            nodo.longitud = -1
            self.nodos.append(nodo)
            self.nodos[ind_min1].longitud = len(self.nodos)-1
            self.nodos[ind_min2].longitud = len(self.nodos)-1

            #comparaciones
            if prob1 >= prob2:
                self.nodos[ind_min1].codificacion = 0
                self.nodos[ind_min2].codificacion = 1

            ind_min1 = self.get_Nodo_minp()
            ind_min2 = self.get_Nodo_minp()

        def obtener_nodo_menor_prob(self):
            minp= 1.0
            index_min = -1

            for index in range ( 0, len(self.nodos)):
                if (self.nodos[index].probabilidad < minp and (not self.nodos[index].visited)):
                    minp = self.nodos[index].probabilidad
                    index_min = index

                elif index_min != -1:
                    self.nodos[index_min].visited = True

            return index_min

        def mostrar_simbolos_codificados(self, simbolo):
            encontrar = False
            index = 0
            codificacion = ""

            for i in range(0,len(self.nodos)):
                if self.nodos[i].simbolo == simbolo:
                    encontrar = True
                    index = i
                    break
            
            if encontrar:
                while index != -1:
                    codificacion = "%s%s"%(self.nodos[index].codificacion,codificacion)
                    index= self.nodos[index].longitud
            else:
                codificacion = "símbolo no conocido"

            return codificacion

        def construcion_dicionario(self):


