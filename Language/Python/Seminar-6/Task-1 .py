# 1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции + , -, /, *. приоритет операций стандартный.

# *Пример: *

# 2+2 = > 4

# 1+2*3 = > 7

# 1-2*3 = > -5

# - Добавьте возможность использования скобок, меняющих приоритет операций.

# *Пример: *

# 1+2*3 = > 7

# (1+2)*3 = > 9
# print(eval(input("Введите значения вырожения")))

from ast import Expression


def parse_symols(full_string):
    res_list = []
    for i in full_string:
        if i in "+-/*":
            res_list.append(i)
    return res_list


def cale(num_list, op_list):
    while len(num_list) > 1:
        if ('*' in op_list) and ('/' in op_list):
            if op_list.index('*') < op_list.index('/'):
                i = op_list.index('*')
                sc = '*'
                
            else:
                i = op_list.index('/')
                sc ='/'
        elif '*' in op_list:
            i = op_list.index('*')
        elif '/' in op_list:
            i = op_list.index('/')
        elif '+' in op_list:
            i = op_list.index('+')
        elif '-' in op_list:
            i = op_list.index('-')


expression = input("Введите значения вырожения: ")
expression - "23+54-47*895/1452+65"
symbs = parse_symols(expression)
expression = list(map(int, (Expression.split(r'\+|\-|\*|\/'))))
print(expression)
print(symbs)
