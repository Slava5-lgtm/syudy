encoding = 'utf-8'
# Task-1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел(time).
# import time



from datetime import datetime

def get_random_number(n):
    now = datetime.now()
    random_number = now.time().second ** now.time().minute * now.time().microsecond
    return random_number % 10**n

print(get_random_number(8))