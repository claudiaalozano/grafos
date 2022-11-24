import os



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
    dictEncoder ={}

    def __init__(self, simbolo):
        self.simbolo = simbolo
        

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
            for simbolo in self.prob:
                codificacion = self.mostrar_simbolos_codificados(simbolo)
                self.dictEncoder[simbolo] = codificacion

        def codificacion(slef, p):
            codificacion = ""
            for simbolo in p:
                codificacion = "%s%s"%(codificacion, self.dictEncoder[simbolo])
            return codificacion

        def descodificar(self):
            index= 0
            descodificar=""
            while index < len(descodificar):
                encontrar= False
                aux = descodificar[index]

                for simbolo in self.prob:
                    if aux.startswith(self.dictEncoder[simbolo]):
                        descodificar = "%s%s"%(descodificar, simbolo)
                        index = index + len(self.dictEncoder[simbolo])
                        break
            return descodificar


if __name__ == "__main__": 
    

    mensaje = "MT130"
    simbolos = ["A", "F", 1 , 3 , 0, "M", "T"]

    p = [0.2, 0.17, 0.13, 0.21, 0.05, 0.09, 0.15]
    msm = mensaje
    d = 0

    for i in mensaje:
        if i in msm:
            simbolos += i
            p.append(float(float(msm.count(i))/float(len(mensaje))))
            msm = msm.replace(i, "")
            d += 1

    simbolo = dict(zip(simbolos,p))

    huffman= Huffman(simbolo)
    print("codificando mediante el árbol de huffman...")
    for simbolo in simbolos:
        print("Simbolo: %S, Codificando:%s"%(simbolo,Huffman.mostrar_simbolos_codificados(simbolo)))

    c= Huffman.codificacion(mensaje)
    print("Mensaje que se esta codificando es ", mensaje)
    print("Codificacion en bits: ", c)
    print("Longitud del mensaje: ", len(mensaje))

    data = c

    print("Ahora vamos a descodificar...")
    de= Huffman.descodificar(data)
    print("El códigp binario para descodificar es: ", data)
    print("El mensaje descodificado es: ", de)
