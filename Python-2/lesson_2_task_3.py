import math


def square(side):
    area = side * side
    if isinstance(side, int):
        return area
    else:
        return math.ceil(area)


side_input = input("Введите длину стороны квадрата: ")
side = float(side_input)

result = square(side)
print(f"Площадь квадрата со стороной {side} равна: {result}")
