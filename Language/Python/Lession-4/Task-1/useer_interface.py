# После того как мы описал логирования(logger), переходим в метод user_interface. Нам нужны (также три кнопочки) или три метода
# которые будут отображать значения погоды, давления и скорости ветра
import imp

import data_provider as prov                                    # Мы будим их откудота брать значит мы их ипортируем из
                                                                # data_provider (чтобы обазначить покороче as prov)

import logger as log                                            # Будем работать с логированием поэтому импрот

# Метод демострируюший информацию о пагоде


def temperature_view(senson):
    data = prov.get_temperature(senson)                         # МЫ будем заберать из нашего провайдера (prov) и вызываем
                                                                # соотвествуюший метод прередовая значения сенсора (senson)
    log.temperature_logger(data)                                # Далее все что нам нужно сделоть это записать в
                                                                # log.temperature_logger(data) инфрмацию ту оторую мы получили то есть
                                                                # это дата
    return data                                                 # И вернем те значения которые мы получили


            # Метод демострируюший информацию о давлении


def pressure_view(senson):
   data = prov.get_pressure(senson)
   log.pressure_logger(data)
   return data

           # Метод демострируюший информацию о скорости ветра


def wind_speed_view(senson):
   data = prov.get_wind_speed(senson)
   log.wind_speed_logger(data)
   return data


# Идем в html_creater
