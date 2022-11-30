                                            # Открытие для чтения данных из файла - 'r'

path = 'file.txt'                           # Создаем путь к нашей папке
data = open(path, 'r')                      # Откроем в режиме чтения
# При помоще цикла (for lie) пробежимся по файлу (in data)
for line in data:                           # При помощи цикла (for line) пробежимся по вфйлу (in data)
 print(line)                                # Считаем все строки
data.close()
