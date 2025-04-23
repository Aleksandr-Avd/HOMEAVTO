import math

def square(side):
    area = side * side 
    return math.ceil(area)

sed = float(input("Сторона квадрата: "))
print(f"Площадь квадрата  {square(sed)}")
