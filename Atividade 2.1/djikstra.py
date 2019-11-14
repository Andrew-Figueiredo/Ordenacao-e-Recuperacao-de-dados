import numpy as np

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
    print(list_vizinhos)
    f.close()
    return size_vertices, Mat, list_vizinhos 


def printPath(distancias,inicio, fim):
        if  fim != inicio:
            return "%s -- > %s" % (printPath(distancias,inicio, distancias[fim][1]),fim)
        else:
            return inicio

def dijkstra_path(grafo, origem, fim): #retorna a menor distancia de um No origem até um No destino e o caminho até ele

    controle = { }
    distanciaAtual = { }
    noAtual = { }
    naoVisitados = []
    atual = origem
    noAtual[atual] = 0

    
    for vertice in grafo.keys():
        naoVisitados.append(vertice) #inclui os vertices nos não visitados    
        distanciaAtual[vertice] = float('inf') #inicia os vertices como infinito
    print(naoVisitados,distanciaAtual)
    distanciaAtual[atual] = [0,origem] 

    naoVisitados.remove(atual)

    while naoVisitados:
        for vizinho, peso in grafo[atual].items():
             pesoCalc = peso + noAtual[atual]
             if distanciaAtual[vizinho] == float("inf") or distanciaAtual[vizinho][0] > pesoCalc:
                 distanciaAtual[vizinho] = [pesoCalc,atual]
                 controle[vizinho] = pesoCalc
                 print(controle)
                 
        if controle == {} : break    
        minVizinho = min(controle.items(), key=lambda x: x[1]) #seleciona o menor vizinho
        atual=minVizinho[0]
        noAtual[atual] = minVizinho[1]
        naoVisitados.remove(atual)
        del controle[atual]

    print("A menor distância de %s atá %s é: %s" % (origem, fim, distanciaAtual[fim][0]))
    print("O menor caminho é: %s" % printPath(distanciaAtual,origem, fim))  


def main():
    try:
        #name = input("Qual Arquivo deseja Usar:")
        #size_vertices, Mat, list_vizinhos = readInstance("instancias/" + "dij10.txt")
       
        grafo = { "A" : { "B" : 1, "C":2 },
          "B" : { "D":2, "E":4 },
          "C" : { "E":2 },
          "D" : { "F": 6 },
          "E" : { "F": 7 },
          "F" : { }
          }

        grafo2 = {  "D" : { "A": 4, "H": 1 },
            "A" : { "H": 10, "E": 1 },
            "H" : { "E": 5, "I": 9 },
            "E" : { "F" : 3 },
            "I" : { "J" : 2 },
            "F" : { "I" : 1, "G": 7, "B": 1, "C": 3 },
            "G" : { },
            "J" : { "G" : 1 },
            "B" : { "C" : 2 },
            "C" : { } }
        dijkstra_path(grafo,"A","F")
        
    except Exception as e:
        print(e)
        return

if __name__ == "__main__":
    main()