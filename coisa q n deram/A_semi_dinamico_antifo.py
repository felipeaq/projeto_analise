import numpy as np
import sys
import heapq
import random
import time
import math

#solucao instavel, pois depende muito de como sera atualizada



class PriorityQueue(list):

    def copy():
        return PriorityQueue(self)


    def add(self,element):
        heapq.heappush(self,element)

    def pop_heap(self):
        return heapq.heappop(self)


def get_min_cost(andares,N):

    custos=np.zeros(N)
    matriz_custos=np.zeros(N,N)
    menor_custo=math.inf
    id_menor_custo=-1

    for i in range (len(N)):
        for j in range (len(N)):
            custo_andar=andares[j]*math.abs(i-j)
            custos[i]+=custo_andar
            matriz_custos[i][j]=custo_andar

        if custos[i]<menor_custo:
            menor_custo=custos[i]
            id_menor_custo=i

    return id_menor_custo, custos,matriz_custos


def atualiza_custos(andares,solution,N):
    pass


def calc_solution(andares,k,N):
    solution = PriorityQueue(N)
    min_cost, table_cost,matriz_custos=get_min_cost(andares)
    solution.add(min_cost)


    for _ in range(1,k):
        pass





def main():


    k,N=tuple(map(int,input().split()))
    andares=np.zeros(N)
    for andar in sys.stdin:
        andares[int(andar)]+=1

    





if __name__=="__main__":
    main()
