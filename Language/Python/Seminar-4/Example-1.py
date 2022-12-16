
# path = file.txt                                       # это выносят строкой и желательно добавить букву r что бы была сырая строка
                                                        # (сырвя строка -  это там где у нас упровляющая последовательность
                                                        # отключаеться если \n - это переход на новую строку)

# file_path = 'file.txt'                                # Путь выносить в отдельную переменую. Усли сделать так уже будет хорошо

#                                                          НО ЛУЧШЕ ТАК:

# from pathlib import Path                                # Это специальная библеотека для работы с путями

# file_path = Path('data', 'test.txt')                     # Создаем путь к нашей папке
# with open(file_path, 'r') as f_data:                    # Откроем в режиме чтения
#     print(f_data.read())#


# Example-1. Считать строку набора чисел из файла. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел. Результат запишите в исодный файл(minn maxx).


f_path = 'test.txt'

with open(f_path, 'r') as f_nums:
    list_nums = f_nums.read().split(' ')
for i in range(len(list_nums)):
    list_nums[i] = int(list_nums[i])

minmax_list = [min(list_nums), max(list_nums)]
with open(f_path, 'a') as min_max:
    min_max.writelines(f"\n {minmax_list} ")