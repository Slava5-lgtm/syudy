                                              # Открытие для чтения данных из файла - 'r'

path = 'file.txt'                             # Создаем путь к нашей папке
data = open(path, 'r')                        # Откроем в режиме чтения
for line in data:                             # При помоще цикла (for lie) пробежимся по файлу (in data)
 print(line)                                  # Ститаем все строки
data.close()
