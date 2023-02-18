def decreasing():
    n = int(input())
    a = (i for i in range(n, 0, -1))
    for i in range(n):
        print(next(a))