import numpy as np
import os
from Grafo import Grafo
from Vertice import Vertice

def readInstance(filePath):

    f = open(filePath,"r")
    size_vertices = int(f.readline())
    Mat = np.zeros((size_vertices,size_vertices),dtype = int)
    list_vizinhos = []
    
    for i in range(size_vertices):
        k = 0
        l = f.readline()
        aux = []
        for j in range(i+1,size_vertices):
            if i!=j:
                Mat[i][j] = int(l.split()[k])
                k+=1
                Mat[j][i] = Mat[i][j]
                if Mat[i][j] != 0  :
                    aux.append(Mat[i,j])
        list_vizinhos.append(aux)                
    
    f.close()
    return size_vertices, Mat, list_vizinhos 

def main():
    try:
        #name = input("Qual Arquivo deseja Usar:")
        size_vertices, Mat, Adj = readInstance("instancias/" + "dij10.txt")
        
        
        graf = Grafo(size_vertices, Mat, Adj)
        graf.initialize_single_source(0)
        graf.displayVertice()
        graf.dijkstra(0)
        
    except Exception as e:
        print(e)
        return

if __name__ == "__main__":
    main()