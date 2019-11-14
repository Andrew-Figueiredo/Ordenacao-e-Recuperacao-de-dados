# -Ordenacao-e-Recuperacao-de-dados
Este Repositório tem fim de mostrar os codigos da disciplina de ordenação e recuperação de dados ministrada no centro de informatica - UFPB

## Atividade 1 - Implementação de Heap Máximo e HeapSort
 O trabalho desenvolvido foi implementado na linguagem python 3.7.3.
 
 O Arquivo *functions.py* apresentado possui as funções criadas para desenvolver o trabalho. As funções criadas e seus respectivos papéis são:
 
 - *swapPositions(A, pos1, pos2) :* Faz a troca dos elemetos do vetor (*pos1* com o *pos2*)
 - *dad(i) :* retorna a posição do pai do nó *i*
 - *left(i) :* retorna a posição do filho esquerdo do nó i (caso exista).
 - *right(i) :* retorna a posição do filho direito do nó i (caso exista).
 - *max_heapify(A, i, size_heap) :* Efetua uma reestruturação no vetor *A* que faz todo arranjo - considerando a posição *i* como pai - se torna uma heap máximo
 - *build_max_heap(A) :* Cria, a partir de um arranjo *A*, uma heap Máximo
 - *heapSort(A) :*  Ordena o arranjo em ordem crescente.

 Já o arquivo *teste.py* estão dois teste proposto.

 - test1().
 - test2().

    Para a execução do código basta digitar *"make run (nome do arquivo)"* e é necessário a versão do Python 3.7.3 para a execução do código. 


**Obs:** Foi adicionado o *0* como primeiro elemento dos vetores pelo fato de Python iniciar sua contagem ed vetores no 0. Ex: vetor = [0, 0, 1, 2, 3, ...].

## Atividade 02 - Implementar Heap-maximun, Max-Heap-Insert, Heap-Extract-Max e Heap-Increase-Key

    Os condigos de cada funções foram implementados no arquivo *function.py* com suas determinadas objetivos:

    - HEAP-MAXIMUN(A):
	retorna o elemento de A com maior valor

    - MAX-HEAP-INSERT(A, x)
    insere o elemento x no conjunto A.
    
    - HEAP-EXTRACT-MAX(A)
	remove e retorna o elemento A de maior chave

    - HEAP-INCREASE-KEY(A, i, x) 
	aumenta o valor da chave do elemento x para o novo valor e que se presume ser maior que o valor atual de x
