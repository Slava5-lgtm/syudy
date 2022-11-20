text = 'съешь ещё этих мягких французских булок'

# help(int)                          - получаем встроеную справку языка Python                    
# print(len(text))                    # сколько в строке количество символов 39
# print('ещё' in text)                # Если наличии под строки в строке (Правда) True
# print(text.isdigit())               # является символы строки цифрами (Ложь) False
# print(text.islower())               # является символы строки нижнего регистра (маленькие буквы) True
# print(text.replace('ещё', 'ЕЩЁ'))   # что то хотим заменить в даом случае еще на ЕЩЕ
# for c in text:
#  print(c)                           # Выводит все символы строки в столбик

print(text[0])  # c
print(text[1])  # ъ
print(text[len(text)-1])  # к
print(text[-5])  # б
print(text[:])  # print(text)
print(text[:2])  # съ
print(text[len(text)-2:])  # ок
print(text[2:9])  # ешь ещё
print(text[6:-18])  # ещё этих мягких
print(text[0:len(text):6])  # сеикакл
print(text[::6])  # сеикакл
text = text[2:9] + text[-5] + text[:2]  # ...
