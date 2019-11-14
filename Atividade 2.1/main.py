import numpy as np
import os
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
                Mat[i][j] = 1#int(l.split()[k])
                k+=1
                Mat[j][i] = Mat[i][j]
                
                if Mat[i][j] != 0  :
                    aux.append(Mat[i,j])
        list_vizinhos.append(aux)                
    print(Mat)
    f.close()
    return size_vertices, Mat, list_vizinhos 

def main():
    try:
        name = input("Qual Arquivo deseja Usar:")
        size_vertices, Mat, list_vizinhos = readInstance("instancias/" + "dij10.txt")
       
        
        
    except Exception as e:
        print(e)
        return

if __name__ == "__main__":
    main()