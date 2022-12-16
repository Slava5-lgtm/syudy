# ПЕРЕДАЧА АРГУМЕНТОВ * args ** kwargs

# ПЕРЕДАЧА НЕ ИМЕНОВАНЫХ АРГУМЕНТОВ  *args

a,b,c = 4,7,8                                           # В несколько переменых можно делать множественое присваевания так же и со
                                                        # списком но если в нашем списке будет будет больше значений чем переменых
                                                        # тогда выдаст ошибку тоже самое будет если значений будет меньше если будет
                                                        # список из двух елементов тогда [a] будет пустая строка []

print(a,b,c)                                            # (a) идет 4, а в (с) идет 5

# Чтобы не было ошибки можно использовать оператор звездачку (*)
# Поставим (*) его всередину
a,*b,c = [True, 7, 8, 'htlo', 9, '54', 67, 4, 3]        # True - идет в переменую (а), 3 - идет в переменую (c), а все что между этими
                                                        # значениями попадают в переменую (b)
print(a,b,c)

# Если поставит ее конец (*)
a, b, *c = [True, 7, 8, 'htlo', 9, '54', 67, 4, 3]      # True - идет в переменую(а), 7 - идет в переменую(b), а все что между этими
                                                        # значениями попадают в переменую (с) и эта переменая предстовляет сабой
                                                        # список
print(a,b,c)

# Если (*) поставим на первое место
*a, b, c = [True, 7, 8, 'htlo', 9, '54', 67, 4, 3]      # В переменую(b) идет предпоследнее зачения, в переменую(с) идет последнее
                                                        # зачения, а переменую(а) все что стоит перед ними
print(a, b, c)

# Фунлция range обходит все цафры от а до b

c = [4, 10]                                               # Есть список (с) состоящий из чисел 4 и 10
print(list(range(1,10)))                                  # это фунция обойдет все цифры от 1 до 5 но что бы их вывести на экран наодо
                                                          # подставить list
print(list(range(*c)))                                    # будет ошибка print(list(range(c))) , но если перед (с) поставить (*)
                                                          # ошибки не будет

def f(a,b,c,d):                                           # есть фунция f которая принемает обязательных четыре аргумента
    print(a,b,c,d)                                        # и печатает их на экран
f(1,2,3,4)                                                # мы можем ее просто вызвать и передать ей четыре аргумента
a = ('htllo',True, 78,[3,4,5])                            # либо можем созать упорядочную колекцию а к таким относяться списки([3,4,5])
                                                          # и кортежи ('htllo',True, 78,)
f(*a)                                                     # будет ошибка так как передаем только одно значение а функция требует что
                                                          # бы передали четыри ну если поставить * то он распакует наш кортеж по
                                                          # переменым: то есть (helo идет в переменую (а)) (True в переменую (b))
                                                          # (78 и переменую (c) и список ([3,4,5] в переменую (d)

# Когда указываем * перед аргументом все передоваемые значения упоковываються в эте переменую () в виде кортеже
def f(*args):                                             # при создании фунции (f) и локальной переменой (*args)
    print(args)

# Мы таже можем создать цикл for и можем обойти элементы кортежа по значению  и подсичать суму всех этих чисел

    s = 0 # для этого создодим локальную переменую s 
    for i in args:
        s += i # и к ней добовляем переменую i
    return s

   

f(1,2,3,56,78,9)                                          # так мы можем передовать произволное количество объектов и они все попали
                                                          # в переменую (args) но в виде кортеджа тоесть не изменяемого обекта

print(f(1,2,3,56,78,9))# Нужно функцию (f) обвернуть в команду (print)
print(f(1,2))
print(f())


# ПЕРЕДАЧА ИМЕНОВАНЫХ АРГУМЕНТОВ ** kwargs

# как можно в функцию передовать именованые аргументы
def f(**kwargs): # Для этог в фунциях ставяться две звездочки (**имя ро желанию)
    # Словори можно обходить при помощи циклов for
    for k, v in kwargs.items(): # Сразу обойдем по ключу и значению при помощи метода items
        print(k, v) 
    print(kwargs)# И это все являеться словорем
f(a=1,b=3,c=5)

# Можно так же комебенировать эти два способа но для этого сперва в оределении указывать (*args, **kwargs) тогда при вызове первые 
# знчения которые передаем будут в виде кортежа, а далее передаем именованые пааметры которые будут упокововатся в словарь