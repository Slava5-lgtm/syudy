                                                    # Открытие для записи данных - 'w'
                                                    # Если изменить данные старые удоляються новые записываються

colors = ['red', 'green', 'blue456']

data = open('file.txt', 'w')                        # Старые данные удоляються новые записываються
data.writelines(colors)
data.close()
