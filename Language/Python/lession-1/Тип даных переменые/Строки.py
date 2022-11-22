text = 'съешь ещё этих мягких французских булок'

print(len(text))  # чтоо бы узнать какое количество символов (len) 39
print('ещё' in text)  # проверить наличия подроски в строке (in) True
print(text.isdigit())  # являются ли все символы строки числами (isdigit())  False
print(text.islower())   # являются ли все символы строки нижнего регистра (маленькие буквы) (islower())True
print(text.replace('ещё', 'ЕЩЁ'))   # что то хотим заменить (replace('еще', 'ЕЩЕ')) еще заменит на ЕЩЕ
for c in text:
 print(c)

