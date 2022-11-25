#grafos
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
