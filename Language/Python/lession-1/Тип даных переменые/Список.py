# numbers = [1, 2, 3, 4, 5]# задаем список
# print(numbers)# выводим список на экран [1, 2, 3, 4, 5]

# ran = range(1, 6)# задаем некоторый список через (range)
# numbers = list(range(1, 6))  # приводим range (range не являеться спмском) к списку
# print(type(ran))
# numbers = list(ran)# привидения типа range к типу list
# print(type(numbers))

# print(numbers)  # [10, 2, 3, 4, 5]
# numbers[0] = 10
# print(f'{len(numbers)} len')
# print(len(numbers))# сколко количества элементов в списке
# print(f'{len(numbers)} len')# воспользовались интерполяцией
# for i in numbers:
#     i *=2# в текущию переменую кладем новое значения (не в список)
#     print(i)# выволд переменых
# print(numbers)# вывод списка

colors = ['red', 'green', 'blue']# создали новый список
for e in colors:# добавили букву е в список
    print(e) # red green blue
for e in colors:
    print(e*2) # redred greengreen blueblue
colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') #del colors[0] # удалить элемент (del colors[0] - удолить элемент под индексом)