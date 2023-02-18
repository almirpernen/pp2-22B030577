def squaresFromAtoB():
    a = int(input())
    b = int(input())
    gen = (int(i)**2 for i in range(a, b + 1))
    for i in range((b-a) + 1):
        print(next(gen))