def squares():
    n=int(input())
    a=(int(i)**2 for i in range(0,n))
    for i in range(n):
        print(next(a))