import numpy as np
import sys
from grafo import *

class Bruto(Linha):
    def __init__(self,hora_atual):
        super().__init__(hora_atual)
        self.caminhos=[]
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
        self.caminhos=[]
        pre=[Rota(None,v,0,1)]
        self.backtr(pre[:],custo=self.hora_atual)



        return self.caminhos_minimos

    def backtr(self,pre,custo=0):

        self.caminhos.append(pre)
        custo_temp=custo+pre[-1].quanto_falta(custo)
        self.constroi_caminhos(custo_temp,pre)

        while(self.linha_to_destroy[pre[-1].p2]):
            pros=self.linha_to_destroy[pre[-1].p2].pop()
            caminho=pre+[pros]
            self.backtr(caminho,custo=custo_temp)



def main():
    hora_atual=int(input())
    d=Bruto(hora_atual)
    for linha in sys.stdin:
        p1,p2,hora_inicio,delay=linha.split()
        d.add_rota(p1,p2,float(hora_inicio),float(delay))
    print (d.forca_bruta("par1"))

if __name__=="__main__":
    print ("exemplo execucao : python3 djkstra.py<teste.txt")
    main()
