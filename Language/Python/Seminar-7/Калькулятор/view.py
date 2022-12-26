def input_data():
    a = input('Введите число: ')
    return a

def input_operation():
    op = input('введите операцию: ')
    return op

    # Переходим в контролер (controller)

def output_res(res, op):
    match op:
        case '+':
            print(f"sum = {res}")
        case '-':
            print(f"diff = {res}")
        case '*':
            print(f"mult = {res}")
        case '/':
            print(f"div = {res}")
        case _:
            print(res)
