# Task 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.

# *Пример: *
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# N = int(input('Введите N: '))
# numbers = list()

# for ei in range(1, N + 1):
#     numbers.append(3*ei + 1)

# print(numbers)

            # через while

n =int (input("Введите N: "))
i = 1
while i <= n:
    print((3*i), end = ', ')
    i +=1