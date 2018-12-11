import numpy as np
import sys
import heapq
import random
import time
import math

#solucao instavel, pois depende muito de como sera atualizada

class Elevador_cost:
    def __init__(self,andares,k,N):
        self.andares=andares
        self.custos=np.zeros(N)
        self.matriz_custos=np.zeros([N,N])
        self.solution = set()
        self.solution_list=[]
        self.k=k
        self.N=N





    def calc_solution(self):

        self.get_min_cost()

        for _ in range(1,self.k):
            self.atualiza_custos()





    def get_min_cost(self):

        menor_custo=math.inf
        id_menor_custo=-1

        for i in range (self.N):
            custo=0
            for j in range (self.N):
                custo+=self.andares[j]*abs(i-j)


            if custo<menor_custo:
                menor_custo=custo
                id_menor_custo=i


        self.solution.add(id_menor_custo)
        self.solution_list.append(id_menor_custo)




    def atualiza_custos(self):
        menor_custo=-math.inf
        id_menor_custo=-1


        for i in range (self.N):
            if i in self.solution:
                continue

            custo=0
            min,max=self.get_min_max(i)

            for j in range (min,max):
                custo+=self.andares[j]*abs(i-j)

            print (i,custo)

            if custo>menor_custo:
                menor_custo=self.custos[i]
                id_menor_custo=i

        self.solution.add(id_menor_custo)
        self.solution_list.append(menor_custo)
        print (self.solution)


    def get_min_max(self,i):
        min,max=self.get_intervalo(i)
        if min==-math.inf:
            min=0
        else:
            min=(i+min+2)//2

        if max==math.inf:
            max=self.N
        else:
            max=((i+max+1)//2)

        #print (i,min,max)

        return min,max





    def get_intervalo(self,i):


        anterior=-math.inf
        for k in self.solution_list:
            if k>i:
                return anterior,k
            anterior=k
        return anterior,math.inf





def main():


    k,N=tuple(map(int,input().split()))
    andares=np.zeros(N)
    for andar in sys.stdin:
        andares[int(andar)]+=1

    Elevador_cost(andares,k,N).calc_solution()








if __name__=="__main__":
    main()
