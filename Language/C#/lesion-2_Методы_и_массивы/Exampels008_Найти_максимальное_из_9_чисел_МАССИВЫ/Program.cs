﻿    // Найти максимальное из 9 чисел (Массивы)
int Max(int arg1, int arg2, int arg3)
{
    int result = arg1;
    if(arg2> result) result = arg2;
    if(arg3> result) result = arg3;
    return result;
}

// Пишем int, затем ставим квадратные скобки, даём какое-то
//наименование и после этого перечисляем значения, которые хотим использовать.

//              0   1   2   3   4   5   6   7   8
int[] array = { 11, 211, 31, 41, 15, 61, 17, 18, 19 };

int max = Max(
    Max(array[0], array[1], array[3]),
    Max(array[4], array[5], array[5]),
    Max(array[6], array[7], array[8])
);
Console.WriteLine(max);

