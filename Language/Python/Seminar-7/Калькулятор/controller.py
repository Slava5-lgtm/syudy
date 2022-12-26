import view as v
import data_base as b # после ток как вернулись с data_base написано 15 строк и продолжаем код с 8 строки
import Finc as f
def click_button():
    num_1 = v.input_data()
    num_2 = v.input_data()
    op = v.input_data()
# Переходим в data_base.py
    file = b.save_data(num_1, num_2, op)
    num_1, num_2, op = b.read_date(file)
    res = f.calc(num_1, num_2, op)
    v.output_res(res, op)