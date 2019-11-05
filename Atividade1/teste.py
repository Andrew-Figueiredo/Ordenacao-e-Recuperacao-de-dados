from functions import heapSort,max_heapify,build_max_heap
import os

def test1(ex1):


    size = len(ex1)
    print ("Vetor:")
    print (ex1[1:size])
    print()
    print("Esolha a posição que deseja operar: ")
    x = int(input())

    if x >= len(ex1) or x <= 0 :
        os.system('cls') or None
        print("Posição invalida!")
    else:
        os.system('cls') or None
        print("\nAntes:")
        print (ex1[1:size])

        ex1 = max_heapify(ex1,x,size-1)
        print(" \nApós a operação Max_Heapify(Vetor, "+ str(x)+").")
        print(ex1[1:size])
        

def test2(ex2):
    
    size = len(ex2)
    os.system('cls') or None
    print ("Vetor:")
    print (ex2[1:size])

    ex2 = heapSort(ex2)
    print(" \nApós a operação HeapSort(Vetor):")    
    print(ex2[1:size])
 



