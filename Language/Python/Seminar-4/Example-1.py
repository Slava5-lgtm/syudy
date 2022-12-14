# from pathlib import Path
# path = file.txt                                       # это выносят строкой и желательно добавить букву r что бы была сырая строка
#                                                        ### НО ЛУЧШЕ ТАК:

# from pathlib import Path                                # Это специальная библеотека для работы с путями

# file_path = Path('data', 'test.txt')                     # Создаем путь к нашей папке
# with open(file_path, 'r') as f_data:                    # Откроем в режиме чтения
#     print(f_data.read())#


# Example-1. Считать строку набора чисел из файла. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел. Результат запишите в исодный файл(minn maxx).


# import json
# from pathlib import Path

# with open(r'C:\\Users\User\\Desktop\\study\\Language\\Python\\Seminar-4\\text.txt' ) as file: # так надо делать путь к файлу
#     text = file.readline()
#     print(text)
#     list_nums = file.read().split(' ')
#     print(list_nums)
# for i in range(len(list_nums)):
#      list_nums[i] = int(list_nums[i])
# minmax_list = [min(list_nums), max(list_nums)]

# with open(text, 'a') as min_max:
#      min_max.writelines(f"\n {minmax_list} ")


from pathlib import Path
file_name = 'text.txt'
relative_file_directory = Path(file_name)
import json

f_path = 'text.txt'
with open(relative_file_directory, 'r', encoding='utf-8') as f_nums:  # так надо делать путь к файлу
    list_nums = f_nums.read().split(' , ')
    # print(f_path)

    print(list_nums)
for i in range(len(list_nums)):
    list_nums[i] = int(list_nums[i])
minmax_list = [min(list_nums), max(list_nums)]


with open(relative_file_directory, 'a') as min_max:
    min_max.writelines(f"\n {minmax_list} ")
print(min_max)
