class Vertice():
    dist = 0
    pai = 0
    esquerdo = 0
    direito = 0
    idHeap = 0
    

    def __init__(self, dist, pai, left, right, idHeap):
        self.dist = dist
        self.pai = pai
        self.esquerdo = left
        self.direito = right
        self.idHeap = idHeap

    def dad(self, i):
        self.pai =  int(i/2)

    def left(self, i):
        self.esquerdo =  int(i*2)

    def right(self, i):
        self.direito = int(i*2 + 1)