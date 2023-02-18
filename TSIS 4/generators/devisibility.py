def devesibility():
    n = int(input())
    x = lambda x : x if (x % 3 == 0 and x % 4 == 0) or x == 0 else "o"
    a = (x(i) for i in range(0, n))
    for i in range(n):
        y = next(a)
        if(y != "o"):
            print(y)