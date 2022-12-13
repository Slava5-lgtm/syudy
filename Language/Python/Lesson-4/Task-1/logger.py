# Как только данные получены мы должны их записать
# Когда дело касаеться логирования чего ли это не было нам точно нужно работать с текушей датой и времением:
# поэтому мы делаем import

from datetime import datetime as dt # импотируем дату as dt - чтобы покороче обращяться
from time import time # импотируем время

                                # Метод отвечающий за логирования температуры
def temperature_logger(data):  
    time = dt.now().strftime('%H:%M') # Импотируем время (вся дата нам не нужна обрашяеся только ко времени во сколько эти даные пришли )
    with open('log.csv', 'a') as file: # oppen('имя файла.(csv - будем работать с псевдо EXEL файломи)', 'a') назавем его file
        
        #file.write('{};temperature;{}\n(time, data') # Сдесь мы указываем file.write(первый аргумент будет '{};temperature; (точка с запятой будет символ разделителем) и вторй аргумет будет выступать то значения которое придет 6 строку (data))'
        file.write('{};temperature;{}\n (time, data')


# Метод отвечающий за логирования давление
def pressure_logger(data):
    
    time = dt.now().strftime('%H:%M')
   
    with open('log.csv', 'a') as file:

        file.write('{};pressure;\n {}time, data')

# Метод отвечающий за логирования скорость ветра
def wind_speed_logger(data):
    
    time = dt.now().strftime('%H:%M')
    
    with open('log.csv', 'a') as file:

        file.write('{};wind_speed;{}\n time, data')

