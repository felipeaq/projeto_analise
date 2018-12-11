import sys
import time
import random
def quick(v,inicio=None,fim=None):
    if inicio==None:
        inicio=0
    if fim ==None:

        fim=len(v)-1



    return quick_r(v,inicio,fim)

def quick_r(v,inicio,fim):
    if inicio<fim:

        pivo=particiona(v,inicio,fim)
        quick_r(v,inicio,pivo-1)
        quick_r(v,pivo+1,fim)
    return v


def particiona(alunos,inicio,fim):
    i = ( inicio-1 )
    pivot = alunos[fim]

    for j in range(inicio , fim):

        if   alunos[j] <= pivot:
            i = i+1
            alunos[i],alunos[j] = alunos[j],alunos[i]

    alunos[i+1],alunos[fim] = alunos[fim],alunos[i+1]
    return ( i+1 )

def teste_empirico_complexidade(N):
        #10x mais lento que a biblioteca padrão (que provavelmente foi implementada)
        #em outra linguagem, mas as duas funções crescem com o mesmo padrao
        v=[]
        for x in range (N):
            v.append(random.random())

        inicio =time.time()
        teste=sorted(v)
        t1 =time.time()-inicio
        inicio=time.time()
        quick(v)
        print (t1,time.time()-inicio)


def teste_corretude(alunos):
    teste=sorted(alunos)
    quick(alunos)
    return "".join(alunos)=="".join(teste)

def teste_com():
    for i in range(1,100000,1000):
        teste_empirico_complexidade(i)


if __name__=="__main__":
    alunos=[]

    for aluno in sys.stdin:
        alunos.append(aluno)
    #teste_com()# - da pra ver que o caso medio eh O(Nlog(N))
    #print(teste_corretude(alunos[:]))# - retorna true
    quick(alunos)
    print ("".join(alunos))
