﻿// Задача для любово количество элементов
int[] array = { 1, 12, 31, 4, 15, 4, 16, 17, 18 }; // Определяем новый массив

int n = array.Length; // Length - возращяет длину или количество элементов в массиве 
int find = 4; // ползователь вводит число

int index = 0; // устанавливаем счетчик

while (index < n) // цикл если index < n
{
    if(array[index] == find) // если алгоритм завершил работу
    {
        Console.WriteLine(index);
        break; // оператор останавливает работу находит первый заданый элемент
    }


    // index + 1;
    index++; // увеличиваем индекс на 1
}