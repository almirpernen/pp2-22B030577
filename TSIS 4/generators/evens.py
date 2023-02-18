def evens():
    n=int(input())
    a=(int(i) for i in range(0, n, 2))
    for i in range(int(n/2)):
        print(next(a), end = ", ")
    print(next(a))