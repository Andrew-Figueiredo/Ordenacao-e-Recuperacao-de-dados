from functions import heapSort,max_heapify,build_max_heap


def test1(ex1):


    size = len(ex1)-1
    print ("Vetor:")
    print (ex1[1:size])
    print()
    print("Esolha a posição que deseja operar: ")
    x = int(input())

    if x >= len(ex1) or x <= 0 :
        print("Posição invalida!")
    else:
        A = max_heapify(ex1,x,size)
        print(" Após a operação Max_Heapify(Vetor, "+ str(x)+").")
        print(A[1:size])

def test2(ex2):
    
    size = len(ex2)-1
    print ("Vetor:")
    print (ex2[1:size])

    ex2 = heapSort(ex2)
    print(" Após a operação HeapSort(Vetor).")    
    print(ex2[1:size])
 



