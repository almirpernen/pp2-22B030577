import math

def polygonArea():
    n = int(input("Input number of sides: "))
    length = int(input("Input the length of sides: "))
    area = (n * length**2) / (4 * math.tan(math.pi/n))
    return f"The area of the polygon is: {round(area)}"