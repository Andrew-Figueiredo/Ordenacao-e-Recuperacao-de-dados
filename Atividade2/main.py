

def readInstance(filePath):

    f = open(filePath,"r")
    size_vertices = int(f.readline())
    Mat = []
    for i in range(size_vertices):
        l = f.readline()
        for j in range(size_vertices):
            if i!=j :
                n = int(l.split()[j])
                Mat.append([i][n])
            
    
    print(Mat)    

    
    f.close()
    return size_vertices, Mat, list_vizinhos 

def main():
    try:
        name = input("Qual Arquivo deseja Usar:")
        vetor = readInstance("instancias/" + "dij10.txt")
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