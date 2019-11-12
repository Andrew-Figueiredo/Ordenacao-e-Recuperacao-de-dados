import numpy as np

def readInstance(filePath):

    f = open(filePath,"r")
    size_vertices = int(f.readline())
    Mat = np.zeros((size_vertices,size_vertices))
    print(Mat)
    for i in range(size_vertices):
        k = 0
        l = f.readline()
        for j in range(i+1,size_vertices):
            if i!=j:
                
                Mat[i][j] = int(l.split()[j])
                k+=1
                print(Mat)
            
            
    
    #print(Mat)    

    
    f.close()
    return size_vertices, Mat, list_vizinhos 

def main():
    try:
        name = input("Qual Arquivo deseja Usar:")
        vetor = readInstance("instancias/" + name)
        #os.system('cls') or None

        #print("Qual exemplo voce quer chamar? ")
        #print("1) Heap Máximo. ")
        #print("2) HeapSort ")

        #op = int(input("\nDigite aqui: "))
        
        #os.system('cls') or None
        
        #if op == 1 :
        #    test1(vetor)
        #elif op == 2 :
        #    test2(vetor)
        #else:
            
        #    print("\nOpção Invalida!")
    except Exception as e:
        print(e)
        return

if __name__ == "__main__":
    main()