# Task 3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

# Пример:

# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

print('Введите число')
n = int(input())
print('[', end='')

for i in range(1, n + 1):
    res = round((1 + 1 / n)**n, 3)
    sum = int(sum([res for res in range(i + 1)]))
    if i < (n + 1) - 1:
        print(f'{sum}', end=', ')
    else:
        print(f'{sum}', end='')
print(']', end='')


