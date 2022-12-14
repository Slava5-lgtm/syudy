# Decorators - это фунцция замыкания (на вход принемает другую функцию)


def decorator(func):                        # Внутри этого декоратора сосдаем вложеную функцию


    def inner():                            # Вложеная функция
        print('start decorator...')         # Внутри функции выкладываем текст декароатор наченаеться ('start decorator...') и о
                                            # том что он заканчиваеться строка 13, а между строками 8 и 13 вызовим ту функцию которя
                                            # нам передовалась внутрь нашего замыкания она нам доступна по имени (func), в четверотой
                                            # строке она поступает в качестве параметра

        func()                              

        print('finish decorator...')        

    return inner                            # И чтобы замыкания получилось мы должны из нашей функции decorator вернуть вложеную
                                            # функцию без вызова тоесть (круглые скобки указавать не нужно)

def say():                                  # Еще для нашего примера нам нужно будет создать какую небудь простую фунцию
    print('hello word')                     # Например ('hello word')

d = decorator(say)
print(d)
d()
t = decorator(say)
t()


# Как до этого у нас рабтали замыкания мы обрашялись к нашей фнкции decorator и передовали другую нашу функцию say и что происходило:
# это функция say поступала в качестве входного аргумента в нашу переменую func и внутри внашей встроеной функции (это строки 7 по
# 15) испльзуем это имя func и получаеться ЗАМЫКАНИЯ которое нам возрощяеться на строке 17 мы могли сохронить его в какую небудь
# переменую (d) строка 23. Вызовим и посмотрим что там будет хрониться, в (d) хрониться функция inir вложеная функция (строки 7 по 17)
# внутри нашего декоратора. Когда вызываем (d()) отробатывает фунция (строки 7 по 15), которая первым делом печатает нам 
# start decorator... потом вызывает нашу функцию каторую мы передали ей это фунция say строка 13 и затем срабатывает print на строке 15 можно создать и другую переменную наример t и тоже передать результат работы этой фунции и тоже ее вызывать

