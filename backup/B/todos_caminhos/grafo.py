

class Previous:
    def __init__(self,prev,dist,prev_list=[]):

        self.prev=prev
        self.dist=dist
        self.prev_list=prev_list
    def __lt__(self,other):
        return self.dist<other.dist

    def __str__(self):
        return "anterior: {} hora de chegada: {}h {}min caminho:{}".format(self.prev,12+int(self.dist//60),int(self.dist%60),self.prev_list)
    def __repr__(self):
        return "|{} |\n ".format(self)



class Rota:
    def __init__(self,p1,p2,hora_inicio,delay):
        self.p1=p1
        self.p2=p2
        self.hora_inicio=hora_inicio
        self.delay=delay

    def quanto_falta(self,hora_atual):
        if self.hora_inicio<hora_atual:
            return (self.hora_inicio-hora_atual)%self.delay
        return self.hora_inicio-hora_atual

    def __repr__(self):
        return "{} (inicio: {}, delay: {}), ".format(self.p1,self.hora_inicio,self.delay)




class Linha:
    def __init__(self,hora_atual):
        self.linha=dict()
        self.hora_atual=hora_atual

    def add_parada(self,nome):
        self.linha[nome]=[]


    def add_rota(self,entrada,destino,hora_inicio,delay):
        if not entrada in self.linha.keys():
            self.add_parada(entrada)
        if not destino in self.linha.keys():
            self.add_parada(destino)

        self.linha[entrada].append(Rota(entrada,destino,hora_inicio,delay))

    def __getitem__(self, key):
        return self.linha[key]

    def quanto_falta_cada(self):
        for paradas in self.linha.values():
            for rotas in paradas:
                print (rotas.quanto_falta(self.hora_atual))






if __name__=="__main__":
    l =Linha()



    l.add_rota("p1","p2",10,40)
    l.add_rota("p1","p3",20, 25)



    l.quanto_falta_cada()



    print (l["p1"])

    #print (l.linha)
