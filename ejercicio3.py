#grafos
import pandas as pd
import networkx as nx
import numpy as np

data = {"Nombre":["Petra","Taj Mahal", "Machu Picchu", "Pirámide de Chichén Itzá", "Coliseo de Roma", "Gran Muralla China", "Cristo Redentor"], "Ubicación":["Jordania", "India", "Perú", "Yucatán", "Roma", " China", "Brasil"], "Tipo":["Arquitectura", "Arquitectura", "Arquitectura", "Arquitectura", "Arquitectura", "Arquitectura", "Arquitectura"]}
df = pd.DataFrame(data, columns=['Nombre', "Ubicación", "Tipo"])
df.to_csv("siete_maravillas", index=False)

Grafo = nx.Graph()
Grafo.add_node("Nombre")
Grafo.add_node("Ubicación")
Grafo.add_node("Tipo")
