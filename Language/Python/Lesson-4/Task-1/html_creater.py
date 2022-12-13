# Первый способ

from useer_interface import temperature_view
from useer_interface import wind_speed_view # далее нам потребуеться извлечь все три метода (3, 4, 5 строка)
from useer_interface import pressure_view

# Дальше нам нужно писать то что и будит генерировать это самый html файл (это делаеться специально библеотекой) но так я этоделать
# не умею буду делать руками

# Опишем этот метод

def create(device = 1):#Будет метод create аргументом может получать какойто device (если с первого зто отрицательные, со второго положительные)
    style = 'style="font-size:22px;"'# Стиль пусть это буден например 22 шрифт
    html = '<html>\n <head></head>\n <body>\n'# Заготовка для этого html предстовления
    html += '   <p {}>Temperature: {} c</p>\n'\
        .format(style, temperature_view(device))# И по факту обычная строка
    html += '   <p {}>Wind_speed: {} m/s</p>\n'\
        .format(style, wind_speed_view(device))
    html += '   <p {}>Pressure: {} mmHg</p>\n'\
        .format(style, pressure_view(device))
    html += '   </boody>\n</html>'

    with open('index.html', 'w') as page:# После этого мы создаем файл index.html
        page.write(html)# И просто его сохроняем

    return html

# На этом html генератор описан делаем точку вхоа отпровляемся в папку mail


def new_create(data, device=1):
    t, p, w = data
    style = 'style="font-size:30px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
    html += '    <p {}>Temperature: {} c</p>\n'\
        .format(style, t)
    html += '    <p {}>Wind_speed: {} m/s</p>\n'\
        .format(style, w)
    html += '    <p {}>Pressure: {} mmHg</p>\n'\
        .format(style, p)
    html += '  </body>\n</html>'

    with open('new_index.html', 'w') as page:
        page.write(html)

    return data




