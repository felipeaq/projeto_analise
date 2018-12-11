import numpy as np
import sys
from grafo import *

class Bruto(Linha):
    def __init__(self,hora_atual):
        super().__init__(hora_atual)

        self.linha_to_destroy={}
        self.caminhos_minimos={}

    def constroi_caminhos(self,custo,caminho):



        x=caminho[-1].p2
        z=caminho[-1].p1
        caminho=caminho[1:]
        previos=Previous(z,custo,caminho)

        if not x in self.caminhos_minimos.keys():
            self.caminhos_minimos[x]=previos

        elif self.caminhos_minimos[x].dist>custo:
            self.caminhos_minimos[x]=previos





    def forca_bruta(self,v):
        self.linha_to_destroy=self.linha.copy()

        pre=[Rota(None,v,0,1)]
        self.backtr(pre[:],custo=self.hora_atual)



        return self.caminhos_minimos

    def backtr(self,pre,custo=0,visited=set()):
        visited.add(pre[-1].p2)

        custo_temp=custo+pre[-1].quanto_falta(custo)
        self.constroi_caminhos(custo_temp,pre)
        #print (self.linha[pre[-1].p2])

        for pros in (self.linha[pre[-1].p2]):


            if not pros.p2 in visited:

                caminho=pre+[pros]
                self.backtr(caminho,custo=custo_temp,visited=visited.copy())



def main():
    hora_atual=int(input())
    entrada=input()
    d=Bruto(hora_atual)
    for linha in sys.stdin:
        p1,p2,hora_inicio,delay=linha.split()
        d.add_rota(p1,p2,float(hora_inicio),float(delay))
    print (d.forca_bruta(entrada))

if __name__=="__main__":
    print ("exemplo execucao : python3 djkstra.py<teste.txt")
    main()
