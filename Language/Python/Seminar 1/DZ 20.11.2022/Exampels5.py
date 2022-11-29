# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между
# ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


import math
print('Введите координату точки A')
numberAX = float(input('X: '))
numberAY = float(input('Y: '))

print('Введите координату точки')
numberBX = float(input('X: '))
numberBY = float(input('Y: '))

a = numberAX - numberBX
b = numberAY - numberBY
c = a * a + b * b
sqrt = round(math.sqrt(c), 3)
print(sqrt)


