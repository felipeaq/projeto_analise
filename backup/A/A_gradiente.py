import numpy as np
import sys
import heapq
import random
import time
import math

class K:
    def __init__(self,k_pos,c_esq,c_dir,n_esq,n_dir,lim_esq,lim_dir):
        self.k_pos=k_pos
        self.c_esq=c_esq
        self.c_dir=c_dir
        self.n_esq=n_esq
        self.n_dir=n_dir
        self.lim_esq=lim_esq
        self.lim_dir=lim_dir

    def __repr__(self):
        return ("{}: (custo_esq: {} |custo_dir: {} |numeros_esq: {} |numeros_dir: {} |lim_esq: {} |lim_dir: {})\n".format(
        self.k_pos,self.c_esq,self.c_dir,self.n_esq,self.n_dir,self.lim_esq,self.lim_dir))

    def __str__(self):
        return "{}: (custo_esq: {} |custo_dir: {} |numeros_esq: {} |numeros_dir: {} |lim_esq: {} |lim_dir: {})".format(
        self.k_pos,self.c_esq,self.c_dir,self.n_esq,self.n_dir,self.lim_esq,self.lim_dir)

    def get_lim(self,other):
        return int((other.k_pos+self.k_pos)//2)



    def update_left_dir(self):
        pass

    '''def walk_dir(andares,left=None,right=None):


        self.c_dir-=self.n_dir # custo da direita = custo da direita - antigo numero de pessoas a direita
        self.n_dir-=self.andares[self.k_pos+1]
        self.n_esq+=self.andares[self.k_pos]
        self.c_esq+=self.n_esq # custo da esquerda = custo da esquerda + novo numero de pessoas a esquerda

        if left!=None:
            new_left_lim=self.get_lim(left)
            if new_left_lim!=self.left_lim:
                pass
        if right!=None:
            pass

'''

    def simulate_movement_cost(self,andares,c_first,n_first,n_second,c_second,direction):

        #print("c_first: {} n_first: {} n_second {}  c_second{}".format(c_first,n_first,n_second,c_second))
        c_first-=n_first # custo da direita = custo da direita - antigo numero de pessoas a direita
        n_first-=andares[self.k_pos+direction]
        n_second+=andares[self.k_pos]
        c_second+=n_second # custo da esquerda = custo da esquerda + novo numero de pessoas a esquerda

        #print("c_first: {} n_first: {} n_second {}  c_second{}".format(c_first,n_first,n_second,c_second))

        return c_first,n_first,n_second,c_second


    def get_lim_cost(self,andares,new_lim):

        return andares[new_lim]*(new_lim-self.k_pos),abs(andares[new_lim])

    def get_dir_cost(self,andares,N,left=None,right=None):

        c_dir,n_dir,n_esq,c_esq=self.simulate_movement_cost(andares,self.c_dir,\
        self.n_dir,self.n_esq,self.c_esq,1)

        #print("######################")
        print (andares)
        print (c_dir,c_esq,"<->",self.c_dir,self.c_esq)
        #print("######################")

        right_left_cost=0
        right_left_n=0
        right_left_lim=0
        left_right_cost=0
        left_right_n=0
        left_right_lim=N

        old_total_cost=self.c_dir+self.c_esq



        if left!=None:
            old_total_cost+=left.c_dir
            new_left_lim=self.get_lim(left)
            if new_left_lim!=self.lim_esq:
                left_right_lim=new_left_lim
                minus_c,minus_n=self.get_lim_cost(andares,new_left_lim)
                c_esq-=minus_c
                n_dir-=minus_n
                plus_c,plus_n =left.get_lim_cost(andares,new_left_lim)
                left_right_cost+=plus_c
                left_right_n+=plus_n
            else:
                left_right_cost=left.c_dir
                left_right_lim=left.lim_dir
                left_right_n=left.c_dir

        if right!=None:

            old_total_cost+=right.c_esq
            new_right_lim=self.get_lim(right)

            if new_right_lim!=self.lim_dir:
                right_left_lim=new_right_lim
                minus_c,minus_n=self.get_lim_cost(andares,new_right_lim)
                c_esq+=minus_c
                n_dir+=minus_n
                plus_c,plus_n =right.get_lim_cost(andares,new_right_lim)
                right_left_cost-=plus_c
                right_left_n-=plus_n
            else:
                right_left_cost=right.c_esq
                right_left_lim=right.lim_esq
                right_left_n=right.c_esq

        total_cost=c_dir+c_esq+left_right_cost+right_left_cost

        return (old_total_cost,total_cost),\
        (c_dir,n_dir,n_esq,c_esq,left_right_lim,right_left_lim),\
        (right_left_cost,right_left_n,right_left_lim),\
        (left_right_cost,left_right_n,left_right_lim)


    def walk_dir(self,andares,N,left=None,right=None):
        #TODO descobrir problema
        costs,self_update,right_update,left_update=self.get_dir_cost(andares,N,left,right)
        print (costs)
        print ("***************")
        print (self_update)
        print (self)
        print ("***************")
        print(right_update)
        print(left_update)
        if costs[0]<costs[1]:
            return False

        if right!=None and right.k_pos-1==self.k_pos:
            return False

        if N-1 == self.k_pos:
            return False



        self.c_dir,self.n_dir,self.n_esq,self.c_esq,self.lim_esq,self.lim_dir=self_update
        self.k_pos+=1
        print (self_update)

        if right!=None:
            right.c_esq,right.n_esq,right.lim_esq=right_update

        if left!=None:
            left.c_dir,left.n_dir,left.lim_dir=left_update
        return True

class Elevador_cost:
    def __init__(self,andares,k,N):
        self.andares=andares
        self.solution = set()
        self.solution_list=[]
        self.k=k
        self.N=N





    def calc_solution(self):

        self.get_min_cost()

        in_loop=True

        count=0
        while in_loop:
            count+=1
            in_loop=False
            anterior=None

            for i,k in (zip(range(len(self.solution_list)),self.solution_list)):
                #print (self.solution_list)

                if i<len(self.solution_list)-2:
                    proximo=self.solution_list[i+1]
                else:
                    proximo=None
                if(k.walk_dir(self.andares,self.N,left=anterior,right=proximo)):
                    in_loop=True
                    print ("A")

                anterior=k
            count+=1
            #if count>5:
            #    break
            print("\n\n\n\n\n\n")
        print (self.solution_list)



        #print (self.solution_list)





    def get_min_cost(self):
         self.start_positions()

    def start_positions(self):
        anterior=0
        k_list=[]
        multiplicador=self.N/self.k
        for i in range (1,self.k+1):
            anterior=(i*multiplicador+anterior)//2

            k_list.append(int(anterior))

        if self.k>1:
            self.first_k(k_list)
            self.middles_k(k_list)
            self.last_k(k_list)

    def calc_cost(self,start,end,k_pos):
        custo=0
        n=0
        print (start,end)
        for i in range(start, end):
            custo+=self.andares[i]*abs(k_pos-i)
            n+=self.andares[i]
        return custo,n

    def first_k(self,k_list):
        custo_esq=0
        custo_dir=0
        n_esq=0
        n_dir=0
        pos_k=k_list[0]
        print (k_list)
        lim_dir=int((k_list[1]+pos_k)//2)
        custo_esq,n_esq=self.calc_cost(0,pos_k,pos_k)
        custo_dir,n_dir=self.calc_cost(pos_k+1,lim_dir,pos_k)


        self.solution_list.append(K(pos_k,custo_esq,custo_dir,n_esq,n_dir,0,lim_dir))

    def init_non_esq(self):
        return self.solution_list[-1].lim_dir,0,0,0,0



    def middles_k(self,k_list):
        for k,k_element in zip(range(1,len(k_list)-1),k_list[1:-1]):
            lim_esq,custo_esq,custo_dir,n_dir,n_esq=self.init_non_esq()
            lim_dir=int((k_list[k+1]+k_element)//2)


            custo_esq,n_esq=self.calc_cost(lim_esq,k_element,k_element)
            custo_dir,n_dir=self.calc_cost(k_element+1,lim_dir,k_element)

            self.solution_list.append(K(k_element,custo_esq,custo_dir,n_esq,n_dir,lim_esq,lim_dir))

    def last_k(self,k_list):
        lim_esq,custo_esq,custo_dir,n_dir,n_esq=self.init_non_esq()
        k_element=k_list[-1]
        lim_dir=self.N
        custo_esq,n_esq=self.calc_cost(lim_esq,k_element,k_element)
        custo_dir,n_dir=self.calc_cost(k_element+1,lim_dir,k_element)
        self.solution_list.append(K(k_element,custo_esq,custo_dir,n_esq,n_dir,lim_esq,lim_dir))






def main():


    k,N=tuple(map(int,input().split()))
    andares=np.zeros(N)
    for andar in sys.stdin:
        andares[int(andar)]+=1

    Elevador_cost(andares,k,N).calc_solution()








if __name__=="__main__":
    main()
