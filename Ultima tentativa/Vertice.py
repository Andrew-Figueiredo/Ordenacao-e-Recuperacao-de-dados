class Vertice():
    dist = 0.
    pi = 0
    idHeap = 0

    def __init__(self, idHeap):
        self.idHeap = idHeap
    
    def setDist(self,dist):
        self.dist = dist

    def setPi(self,pi):
        self.pi = pi

    def getDist(self):
        return self.dist
    
    def getPi(self):
        return self.pi
    
    def getIdHeap(self):
        return self.idHeap
    