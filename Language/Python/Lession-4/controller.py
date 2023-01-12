# controller он должен работать с нашей моделью (module, view)

import module
import view

def button_click():
    value_a = view.get_value() # Внутри нашей модели должен быть токой метод
    value_b = view.get_value()# После создания строк 7 8 возврошяемся в папку view
    module.init(value_a, value_b)# Производим иницелизацию начальных значений передав соотвествуюшие аргументы (value_a, value_b)
    result = module.sum() # После этого нам потребуеться вычеслить сумму
    view.view_data(result) # И после этого опять вернуть значеня нашего метода view_data и отдаем результат (result)

# После создания 11 строки создаем папку main.py
