# Функция map() применяет указанную функцию к каждому элементу итерируемого объекта и возвращает итератор с новыми объектами.

li = [x for x in range(1, 20)]                  # Создали список

# li = map(lambda x:x+10, li)                   # Хотим получит новый набор данных через исползования функции (map) в качестве
                                                # первого аргумент передаем (lambda x:x+10) которое увеличевает число на 10 а
                                                # в качестве второго аргумента непосредствено нобор данных (li) запускаем 
                                                # ощибок нету но выходит это сообшения map object

li = list(map(lambda x:x+10, li))               # Все что нам требуеться превратить его в список и все хорошо

print(li)