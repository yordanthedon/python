import math

figure = input()
area = 0
if figure == "square":
    a = float(input())
    area = a * a
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
elif figure == "circle":
    r = float(input())
    area = math.pi * (r ** 2)
elif figure == "triangle":
    a = float(input())
    b = float(input())
    area = 1 / 2 * a * b
print(f"{area: .3f}")
