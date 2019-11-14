from Vertice import Vertice
from functions_aux import heapSort
infinity = float("inf")
import copy as cp

class Grafo():
    vertices = []
    Mat = []
    Adj = []

    def __init__(self, n, Mat, Adj):
        for i in range(n):
            aux = Vertice(i)
            self.vertices.append(aux)
        self.Mat = Mat
        self.Adj = Adj

    def getVertices(self):
        return self.vertices

    def initialize_single_source(self, s):
        for v in self.vertices:
            v.setDist(infinity)
            v.setPi(-1)
        self.vertices[s].setDist(0)
    
    def relax(self, u, v):
        
        if v.getDist() > u.getDist() + self.Mat[u.getIdHeap(),v.getIdHeap()] :
            v.setDist(u.getDist() + self.Mat[u][v])
            v.setPi(u.getIdHeap())

    def extract_min(self, Q):
        Q = [i.getIdHeap() for i in self.vertices]

        return Q[1]

    def dijkstra(self, s):
        self.initialize_single_source(s)
        S = []
        Q = [i.getIdHeap() for i in self.vertices]
        while Q != []:
            u = self.extract_min(Q)
            S.append(u)
            for v in self.Adj:
                self.relax(u,v)

    def displayGrafo(self):
        for v in self.vertices:
            print(v.getIdHeap())

    def displayVertice(self):
        for v in self.vertices:
            print(
                "\nDist: "+str(v.getDist())+
                "\nPi: " + str(v.getPi()) +
                "\nIdHeap: " + str(v.getIdHeap()) 
                )

    