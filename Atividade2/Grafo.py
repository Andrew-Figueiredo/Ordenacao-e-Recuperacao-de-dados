import Vertice

class Grafo():
    vertices = [Vertice]

    def __init__(self, vertices):
        self.vertices = vertices


    def swapPositions(self, pos1, pos2): 
        self.vertices[pos1], self.vertices[pos2] =  self.vertices[pos2], self.vertices[pos1] 
        

    def max_heapify(self,A, i, size_heap ):
        l = A.left(i)
        r = A.right(i)
        if l <= size_heap and A [l] > A[i] :
            best = l
        else:
            best = i
        
        if r <= size_heap and A[r] > A[best] :
            best = r
        if best != i :
            self.swapPositions(i,best)
            max_heapify(A,best,size_heap)
        return A

    def min_heapify(self, A, i, size_heap ):
        l = left(i)
        r = right(i)
        if l <= size_heap and A[l] < A[i] :
            best = i
        else:
            best = l
        
        if r <= size_heap and A[r] < A[best] :
            best = r
        if best != i :
            A = swapPositions(A,i,best)
            min_heapify(A,best,size_heap)
        return A

    def build_max_heap(self, A):
        length = len(A)-1
        size_heap = length
        for i in range(int(length/2), 0, -1):
            max_heapify(A,i,size_heap)
        return length, size_heap

    def build_min_heap(self, A):
        length = len(A)-1
        size_heap = length
        for i in range(int(length/2), 0, -1):
            min_heapify(A,i,size_heap)
        return length, size_heap

    def heapSort(self, A):
        length, size_heap = build_max_heap(A)
        for i in range(length, 0, -1):
            swapPositions(A,1,i)
            size_heap -= 1
            max_heapify(A,1,size_heap)
        return A

    def heap_maximun(self, A):
        return A[1]

    def heap_extract_max(self, A):
        size_heap = len(A)-1
        if (size_heap < 1):
            return print("heap underflow")
        max = A[1]
        A[1] = A[size_heap]
        size_heap-=1
        A = max_heapify(A,1,size_heap)
        return max

    def heap_increase_key(self, A,i,key):
        if(key < A[i]) :
            return print( "nada a ser feito")
        A[i] = key
        while(i > 1 and A[ dad(i) ] < A[ i ]):
            self.swapPositions(A, A[i], A[ dad(i) ])
            i = dad(i)
    def max_heap_insert(self, A,key):
        size_heap = len(A)-1
        size_heap += 1
        A[size_heap] = -inf
        heap_increase_key(A,size_heap,key)
