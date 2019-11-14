class Vertice():
    dist = 0
    pi = 0
    idHeap = 0
    

    def __init__(self, dist, pi, idHeap):
        self.dist = dist
        self.pi = pi
        self.idHeap = idHeap

    def dad(self, i):
        return  int(i/2)

    def left(self, i):
        return  int(i*2)

    def right(self, i):
        return int(i*2 + 1)