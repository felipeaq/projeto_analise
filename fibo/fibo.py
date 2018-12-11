def fibo(i):
    if (i<2):
        return i
    else:
        return fibo(i-1)+fibo(i-2)

if __name__=="__main__":
    for i in range (10):
        print (fibo(i))
