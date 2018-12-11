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


def get_min_cost(andares,N,solucoes):

    id_menor_custo=-1
    menor_custo=math.inf

    for i in range (len(N)):
        custo_andar=0
        for j in range (len(N)):
            custo_andar+=andares[j]*math.abs(i-j)

        if custos[i]<menor_custo and not i in solucoes:
            menor_custo=custo_andar
            id_menor_custo=i

    return id_menor_custo


def atualiza_custos(andares,solution,N):
    pass


def calc_solution(andares,k,N):
    solution = set()


    for _ in range(1,k):
        solution.add(get_min_cost())





def main():


    k,N=tuple(map(int,input().split()))
    andares=np.zeros(N)
    for andar in sys.stdin:
        andares[int(andar)]+=1







if __name__=="__main__":
    main()
