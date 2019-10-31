from teste import test1,test2
import os
# Pode ser feito alteração no vetor
vetor = [ 0, 3, 5, 2, 7, 13, 1, 15, 10, 4, 8]

if __name__ == "__main__":
    os.system('cls') or None
    print("Qual exemplo voce quer chamar? ")
    print("1) Heap Máximo. ")
    print("2) HeapSort ")
    op = int(input("\nDigite aqui: "))
    os.system('cls') or None
    if op == 1 :
        test1(vetor)
    elif op == 2 :
        test2(vetor)
    else:
        
        print("\nOpção Invalida!")

