# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

#     *Примеры:*

#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

a = int(input("Введите число: "))
b = -a

if a < b:

    min = a
    max = b
else:
    min = b
    max = a

numbers = list()
for i in range(min, max+1):
    numbers.append(i)
print(numbers)


# Параметр sep
# Рассмотрим следующий код:

# print('a', 'b', 'c')
# print('d', 'e', 'f')
# Результатом выполнения такого кода будет:

# a b c
# d e f
# Рассмотрим следующий код:

# print('a', 'b', 'c', sep='*')
# print('d', 'e', 'f', sep='**')
# Результатом выполнения такого кода будет:

# a*b*c
# d**e**f
# При первой печати в качестве строки разделителя между аргументами команды print() установлена строка sep = '*'.

# При второй печати в качестве строки разделителя между аргументами команды print() установлена строка sep = '**'.

# Таким образом, необязательный параметр sep команды print() позволяет установить строку, с помощью которой будут разделены аргументы при печати.
