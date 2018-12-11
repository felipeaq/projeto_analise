from math import inf
import heapq
import numpy as np
import sys
from grafo import *




class PriorityQueue(list):
    def pop(self):
        return heapq.heappop(self)

    def push(self,item):
        heapq.heappush(self,item)





class Djkstra(Linha):
    def __init__(self,hora_atual):
        super().__init__(hora_atual)
        self.prev_list={}
        self.visitados=set()
        self.pq=PriorityQueue()

    def init_djkstra(self,v):
        self.prev_list={}
        for g in self.linha.keys():
            self.prev_list[g]=Previous(None,inf)

        self.prev_list[v].dist=self.hora_atual
        self.vistitados=set([v])
        self.pq.push(Previous(v,self.hora_atual))


    def djkstra(self,v):

        self.init_djkstra(v)

        while(self.pq):
            v=self.pq.pop()
            self.hora_atual=v.dist
            self.visita_visinhos(v)

        return self.prev_list

    def visita_visinhos(self,v):

        self.visitados.add(v.prev)
        for _v in self.linha[v.prev]:

            #while(self.pq)*for _v in self.linha[v]=O(E)
            peso_atual=v.dist +_v.quanto_falta(self.hora_atual)
            caminho_total=v.prev_list+[_v]
            
            if not _v.p2 in self.visitados:
                self.pq.append(Previous(_v.p2,peso_atual,caminho_total))

                #O(E*k*log(v)))=O(Elog(v))

            if peso_atual<self.prev_list[_v.p2].dist:
                self.prev_list[_v.p2]=Previous(v.prev,peso_atual,caminho_total)

                #O(E*K)







def main():
    hora_atual=int(input())
    d=Djkstra(hora_atual)
    for linha in sys.stdin:
        p1,p2,hora_inicio,delay=linha.split()
        d.add_rota(p1,p2,float(hora_inicio),float(delay))



    print(d.djkstra("par1"))
    #print(d.djkstra("par1")["par2"])

if __name__=="__main__":
    print ("exemplo execucao : python3 djkstra.py<teste.txt")
    main()
