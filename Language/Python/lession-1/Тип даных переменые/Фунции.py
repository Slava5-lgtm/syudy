# ЗАПУСКАЕМ С 1 ПОЛУЧАЕМ ЦЕЛОЕ И КЛАСС СТРОКА
# ЗАПУСКАЕМ С 2.3 ПОЛУЧАЕМ 23 И КЛАСС ДАННЫХ int
# ЗАПУСКАЕМ С ДРУГИМ ЗНАЧЕНИЕМ НАПРИМЕР С 2 НЕ ЧЕГО (None) И ТИП ДАНЫХ None Type 



def f(x):# ключивое слово def имя f аргументы (x):
    if x == 1:# миксуем типы вазрощяемых значений т.е убераем точку
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return


arg = 1  # АРГУМЕНТ (arg) = 1
print(f(arg))# ПОКАЗЫВАЕМ РЕЗУЛЬТАТ РАБОТЫ arg САМОЙ ФУНЦИИ
print(type(f(arg)))# СДЕСЬ ПОКАЗЫВАЕМ ТИП ДАНЫХ
