# Task 5 Реализуйте алгоритм перемешивания списка.

import random

# initializing list инициализирующий список
test_list = [1, 4, 5, 6, 3]

# Printing original list Печать оригинального списка
print("Первоначальный список таков : " + str(test_list))

# using random.sample() использование random.sample()
# to shuffle a list  чтобы перетасовать список
res = random.sample(test_list, len(test_list))

# Printing shuffled list Печать перетасованного списка
print("Перемешеный список : " + str(res))
