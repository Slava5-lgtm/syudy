# Task3. Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой
# Я люблю Python
# 'лю'
# 2

str_test = input('строка: ')                            # Ввели строку
str_count = input('подстрока: ')                        # Определить какая нужна подстрока

# print(str_test.count(str_count))                      # Определили сколько в строке подстроки

counter = 0
for el in range(0, len(str_test)):                      #                      
    if str_count == str_test[el:len(str_count)+el]:     #
        counter += 1                                    #
print(counter)                                          

s1 = input('Введите строку: ')
s2 = input('Какая нужна подстрока: ')
print(s1.count(s2))

# s1 = '125567893788123123123893'
# print(s1.split('3')) # split('3') - будет разбивать строку и остонавливаться на 3 