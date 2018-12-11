from math import inf
import heapq
import numpy as np
import sys
from grafo import *

class Previous:
    def __init__(self,prev,dist):

        self.prev=prev
        self.dist=dist
    def __lt__(self,other):
        return self.dist<other.dist

    def __str__(self):
        return "anterior: {} distancia: {}".format(self.prev,self.dist)
    def __repr__(self):
        return "|{} |\n ".format(self)

class Nodo:
    def __init__(self,nodo,peso):
        self.nodo=nodo
        self.peso=peso

    def __str__(self):
        return "nodo:{} peso:{}".format(self.nodo,self.peso)

class Graph:
    def __init__(self):
        self.graph={}

    def add_nodo(self,node):
        self.graph[node]=[]

    def add_aresta(self,node,destino,peso):
        if not node in self.graph.keys():
            self.add_nodo(node)
        if not destino in self.graph.keys():
            self.add_nodo(destino)
        self.graph[node].append(Nodo(destino,peso))


class Djkstra:
    def __init__(self, grafo):
        self.grafo=grafo
        self.prev_list={}
        self.visitados=set()
        self.percorrido=0

        self.pq=[]

    def djkstra(self,v):
        self.percorrido=0
        self.prev_list={}
        for g in self.grafo.graph.keys():
            self.prev_list[g]=Previous(None,inf)
        self.prev_list[v].dist=0
        self.vistitados=set([v])

        self.pq=[Previous(v,0)]


        while(self.pq):
            v=heapq.heappop(self.pq)
            self.percorrido=v.dist
            self.visita_visinhos(v.prev)
        return self.prev_list

    def visita_visinhos(self,v):

        self.visitados.add(v)
        for _v in self.grafo.graph[v]:
            #while(self.pq)+for _v in self.grafo.graph[v]=O(E)
            peso_atual=_v.peso+self.percorrido
            if not _v.nodo in self.visitados:
                heapq.heappush(self.pq,Previous(_v.nodo,peso_atual))
                #O(E(log(v)+k))=O(Elog(v))

            if peso_atual<self.prev_list[_v.nodo].dist:
                self.prev_list[_v.nodo]=Previous(v,peso_atual)
                #O(E*K)







def main():
    g=Graph()
    for linha in sys.stdin:
        v1,v2,peso=linha.split()
        peso=float(peso)
        g.add_aresta(v1,v2,peso)

    d=Djkstra(g)


    print(d.djkstra("1"))

if __name__=="__main__":
    print ("exemplo execucao : python3 djkstra.py<teste.txt")
    main()
