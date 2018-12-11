def fatorial(i):
    if i<2:
        return 1
    return i*fatorial(i-1)


if __name__=="__main__":
    print (fatorial(6))
