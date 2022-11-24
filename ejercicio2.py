import csv
import pandas as pd

#f = open("pokemon.csv")
#reader = csv.reader(f)
#for row in reader:
    #print(row)

data = pd.read_csv("pokemon.csv", header = 0)
print(data)



class Nodo:
    def __init__(self,dato):
        self.dato = dato 
        self.izquierda = None 
        self.derecha = None 
