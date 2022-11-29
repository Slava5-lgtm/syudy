# тип данных и переменная
# int, float, boolean, str, list, None
value = None
#print = (type(value))
a = 123 # целое
b = 1.23 # вешественое
print(a) # вывести на экран
print(b)
value = 12334
print(value)
a = 123  # целое
b = 1.23 # вешественое
# print(type(a)) # вывести на экран и показать кокой будет тип даных
# print(type(b))
value =12334
# print(type(value))
s = 'hello world' # строка
# s = "hello 'world" # внутри строки использывать ковычкой  
# s = 'hello "world' # внутри строки использывать двойные ковычки
# s = 'hello \nworld' # переход на новую стоку
print(s) # вывод строки
# print(a, b, s) #выводит все в одну строку
print(a,'-',b, '-',s) # ставим между ними дополнительные даные
print('{} - {} - {}'.format(a, b, s)) # 24 и 25 одинаково
#print(f'{a} - \n{b} - {s}'.format(a, b, s))
print('{1} - {2} - {0}'.format(a, b, s)) # куда какие значенее переменой подстовляються

