# Передача данных в клиент-серверных проектах
# Хранение конфигов
# Логирование действий
# Как работать с файлами:
# Связать файловую переменную с файлом,
# определив модификатор работы
# a – открытие для добавления данных
# r – открытие для чтения данных
# w – открытие для записи данных

                                    # Открытия и добовления данных - 'a'
colors = ['red', 'green', 'blue']                   # Есть некоторый набор данных (в качестве набора выстутает список)
                                                    # выступает список)
data = open('file.txt', 'a')                        # Сооздаем текстовую переменую data и связываем ее с
                                                    # текстовым файлом
                                                    # Функция open
                                                    # (['file.txt', 'a') 'file.txt' - путь к файлу,
                                                    # 'a' указываем модификатор с которым будем работать

data.writelines(colors)                             # writelenes - функция позволяющая запичать некоторый
                                                    # набор даных
                                                    # (colors) в качестве аргумента передаем набор данных
                                                    # не будет не коких разделителей (все будет писаться слитно)
data.close()                                        # закрытия файла

                                                     # Открытие для записи данных - 'w'
                                                    # Если изменить данные старые удоляються новые записываються

