from functions import heapSort,max_heapify,build_max_heap
   
A = [ 0,27, 17, 3, 16, 13, 10, 15, 7 , 12, 4, 8, 9, 0]
#A = [0,4,1,3,2,16,9,10,14,8,7]
#A = [0,8,9,7,16,10,14]
print(A)
#a,b = build_max_heap(A)
A = heapSort(A)
# A = max_heapify(A,3)


print(A)