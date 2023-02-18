import math

def trapezoidArea():
    h = int(input("Height: "))
    a = int(input("Base, first value: "))
    b = int(input("Base, second value: "))
    area = ((a + b) / 2) * h
    return area