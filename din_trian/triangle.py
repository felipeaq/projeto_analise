import sys
class Triangle(list):

    def add_num(self,linha):
        self.append(list(map(int,linha.split())))

    def get_min(self):
        mem=self[-1][:]

        for i in range(len(self)-2,-1,-1):
            for j in range(len(self[i])):
                mem[j]=self[i][j]+min(mem[j],mem[j+1])


        return mem[0]


def main():
    t =Triangle()

    for linha in sys.stdin:
        t.add_num(linha)

    print (t)

    print (t.get_min())

if __name__=="__main__":
    main()
