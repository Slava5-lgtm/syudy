# Модуль который будет постовлять нам даных
from random import randint # Модуль генерации псевдо случайных чисел

def get_temperature(sensor): # получиния температуры
    return randint(-20,0) if sensor else randint(0,20)


def get_pressure(sensor):
    #return randint(720, 750) if sensor else randint(750, 770)
    if sensor:
        return randint(720, 750)
    else:
        return randint(750, 770)
    

def get_wind_speed(sensor):
    if sensor == 1: 
        return randint(0, 30) 
    else:
        return randint(30, 50)

# Покамес на этом остановимся следуший модуль каторый будем описывать - моуль logger в него

#  Выше прграма работает

# ОПИСЫВАЕ ДОПОЛНИТЕЛЬНЫЙ МЕТОД КОТОРЫЙ БУДЕТ СОБИРАТЬ ДАННЫЕ СО ВСЕХ ДАТЧИКОВ И ОТДОВАТЬ ИХ ОДНОЙ ПОРЦЕЕЙ

def data_coolecnion():# Назавем его data_collection
    return (get_temperature(), get_pressure(), get_wind_speed())  # Описывае кортеж тепературу, давления и скорость ветра

# далее надо в модуле html сделать поправки