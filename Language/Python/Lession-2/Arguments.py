                                        # НЕОГРОНИЧЕНОЕ (ЛЮБОЕ) КОЛИЧЕСТВО АРГУМЕНТОВ В ФУНЦИИ


def concatenatio(*params):              # Перред аргументом ставим * (*params)
 res: str = ""                          # Тип даных строка
 #res: int = 0                          # Делать этого не стоит но технически можно
 for item in params:                    # Логика завязана как работа со строкой
    res += item
 return res


print(concatenatio('a', 's', 'd', 'w'))  # Вызываме фунцию передаем четыре аргумента и получаем строку asdw
print(concatenatio('a', '1', 'd', '2'))  # Или передаем два аргумента и получаем 1d2
# print(concatenatio(1, 2, 3, 4))  