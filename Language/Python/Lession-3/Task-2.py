# С клавеатуре вводиться некий набор чисел считываем мы в строковом предстовлении в качестве символа рзделителя пусть будет пробел


# data = list(map(int,input().split()))                         # Есть набор данных рзбиваем при помощи (split если вкачестве
                                                                # разделителя будет использоваться запятая можно указать следушим
                                                                # оброзом (',') (по умлчанию используются пробелы)) здесь мы получаем
                                                                # список который будем пробрасывать в функцию (map) в качестве
                                                                # аргумента (будим передовать фунцию int) превращяющего лист из строк
                                                                # в лист чисел 
# print(data)                                                   # И мы снова получаем (map object)

# data = list(map(int, input().split()))                        # Соотвествно что бы все исправит надо в эту строку
                                                                # (data=(map(int, input().split())))
                                                                # просто поставит(data=list(map(int, input().split())))
# print(data)


                                                        # ЧТО ЗДЕСЬ ВАЖНО


# data = map(int, input().split())                              # Технически можно е делат преоброзования к типу
                                                                # list(data=(map(int, input().split())))

# for e in data:                                                # А сразу же пробежаться по соотвествуюшим обектам
#     print(e)

# data = map(int,'1 2 3 56 987'.split())                        # Что быне вводить постояно с клавиатуры место (input() доставим цифры
                                                                #  '1 2 3 56 978')
# for e in data: 
#     print(e)

# for e in data:
#     print(e)                                                  # И продублируем код еше раз
# print('--')                                                   # Сделав ввывод условного разделителя (print('--))
# for e in data:                                                # И хотим на этих строках получить еще один набор данных
#     print(e)


# map - Результат работы map это некий эпиратор по (эпиратору можно пробежаться только один раз) соотвествено что бы работать
# несколько раз одними и теже ми даными мы должны где то принудительно сохранить в качестве этого пронудительн специально и указывают
# list(map(int, '1 2 3 56 987')).split())

encoding = 'utf-8'

data = list(map(int, '1 2 3 56 987'.split()))
for e in data:
    print(e)

for e in data:
    print(e)  
print('--')  
for e in data: 
    print(e)
