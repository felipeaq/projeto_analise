import sys

class Nodo:
    def __init__(self,v1,v2,peso):
        self.v1=v1
        self.v2=v2
        self.peso=peso


    def __repr__(self):
        return "({}, {}, {}),   ".format(self.v1,self.v2,self.peso)
class Grafo:
    def __init__(self,lista_nodos=[],lista_vertices=set()):
        self.lista_nodos=lista_nodos
        self.lista_vertices=lista_vertices

    def add_vertice(self,v):
        self.lista_vertices.add(v)

    def add_nodo(self,nodo):

        if not nodo.v1 in self.lista_vertices or not nodo.v2 in self.lista_vertices:
            self.lista_vertices.add(nodo.v1)
            self.lista_vertices.add(nodo.v2)

        self.lista_nodos.append(nodo)

    def join(self,grafo,nodo_ponte):
        self.lista_nodos+=grafo.lista_nodos
        self.lista_vertices=self.lista_vertices.union(grafo.lista_vertices)
        self.add_nodo(nodo_ponte)

    def __repr__(self):

        return "{} ,--------------, ".format(self)


    def __str__(self):
        return "{} <<<>>> {}".format(self.lista_nodos,self.lista_vertices)


class Kruskal:


    def __init__(self,grafo):
        self.lista_nodos=sorted(grafo.lista_nodos,key=lambda x : x.peso,reverse=True)
        self.numero_vertices=len(grafo.lista_vertices)

        self.grafo=Grafo([],set())

        self.grafos=[]
        #print (self.lista_nodos)

    def gera_arvore(self,nodo):

        id1=-1
        id2=-1

        for g,count in zip(self.grafos,range(len(self.grafos))):

            if nodo.v1 in g.lista_vertices:
                id1=count

            if nodo.v2 in g.lista_vertices:
                id2=count

        if id1==-1 and id2==-1:

            self.grafos.append(Grafo([nodo],set([nodo.v1,nodo.v2])))
        elif id1==id2:
            return
        elif id1!=-1 and id2!=-1:
            self.grafos[id1].join(self.grafos[id2],nodo)
            self.grafos.pop(id2)

        elif id1!=-1:
            self.grafos[id1].add_nodo(nodo)

        elif id2!=-1:
            self.grafos[id2].add_nodo(nodo)

        return





    def kruskal (self):


        while(len(self.grafo.lista_nodos))<self.numero_vertices-1:
            #print(self.lista_nodos)

            nodo=self.lista_nodos.pop()

            if nodo.v1==nodo.v2:
                continue

            self.gera_arvore(nodo)
            self.grafo=self.grafos[0]



        return self.grafo


def testa_kruskal():
    g=Grafo()
    for linha in sys.stdin:
        v1,v2,peso=linha.split()
        peso=float(peso)
        g.add_nodo(Nodo(v1,v2,peso))
    print(g)
    print("\n\n\n***********************\n\n\n")
    k=Kruskal(g)
    #k.kruskal()
    print(k.kruskal())







if __name__=="__main__":
    testa_kruskal()
