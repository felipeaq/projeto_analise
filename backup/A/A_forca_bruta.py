import numpy as np
import sys

def dist_mais_prox(andar,pontos):
    ''' descobre qual o nadar mais proximo complexidade: O(K)'''
    min=np.inf
    for ponto in pontos:
        distancia=abs(andar-ponto)
        if min>distancia:
            min=distancia
    return min

def calula_distancia(andares,pontos):
    '''calula o quanto cada pessoa vai ter que andar. complexidade: O(N*K)'''
    distancia=0
    for i in range(len(andares)):
        distancia+=andares[i]*dist_mais_prox(i,pontos)

    return distancia

def main():


    k,N=tuple(map(int,input().split()))
    andares=np.zeros(N)
    for andar in sys.stdin:
        andares[int(andar)]+=1
    print (forca_bruta(andares,k))
    #forca_bruta(andares,k)



def forca_bruta(andares, k):
    '''testa todas as possibilidades. Complexidade: O(N^K*N*K)ou simplificando O(N^K)'''
    min_dist=np.inf

    pontos=np.zeros(k, dtype=int)
    melhor_soluc=np.zeros(k,dtype=int)

    if k>=len(andares):
        return pontos
    cont=0
    for i in range((len(andares))**k):
        cont+=1
        dist=calula_distancia(andares,pontos)

        print (pontos, dist)

        if dist <min_dist:
            min_dist=dist
            np.copyto(melhor_soluc, pontos)

        i=0

        pontos[i]=(pontos[i]+1)%(len(andares))

        while (i<k-1 and pontos[i]==0):
            i+=1
            pontos[i]=(pontos[i]+1)%(len(andares))


    return melhor_soluc

if __name__=="__main__":
    main()
