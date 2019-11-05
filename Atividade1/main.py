from teste import test1,test2
import os
import sys
def readInstance(filePath):

    f = open(filePath,"r")
    vetor = f.readlines()
    for i in range(len(vetor)):
        vetor[i] = int(vetor[i])

    f.close()
    return vetor



def main():
    try:
        name = input("Qual Arquivo deseja Usar:")
        vetor = readInstance("instancias-num/" + name)
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
    except Exception as e:
        print(e)
        return

if __name__ == "__main__":
    main()
    
