def save_data(a, b, op):
    file = 'cash.txt'
    with open(file, 'w') as d:
        d.writelines(a)
        d.writelines(b)
        d.writelines(op)
    return file


def save_data(file: str):
    with open(file, 'r') as d:
       a = int(d.readline())
       b = int(d.readline())
       op = int(d.readline())
       return a, b, op



# Возврощяемся в котролер
