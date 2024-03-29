﻿// Теперь попробуем воспользоваться знаниями с предыдущих лекций и опишем метод, который будет
// отдельно печатать двумерную матрицу на экран и заполнять её числами. Итак, поехали.
// Учитывая тот факт, что мы плюс-минус знаем, как это делается, можем немножко схитрить. Для
// текущего кода сделаем обрамление в виде метода. Делаем отступы, чтобы всё было красиво. В
// качестве аргумента передаём прямоугольную таблицу чисел. Вместо matrix будем передавать
// сокращённое название — matr. Метод PrintArray в качестве аргумента принимает двумерную таблицу
// чисел и будет печатать её на экран. В качестве аргумента передаём ту матрицу, которая была
// определена чуть раньше. Чтобы код был более скомпонованным, инициализацию массива перенесём
// поближе к вызову печати.

void PrintArray(int[,] matr)
{
    for (int i = 0; i < matr.GetLength(0); i++)
    {
        for (int j = 0; j < matr.GetLength(1); j++)
        {
            Console.Write($"{matr[i, j]} ");
        }
        Console.WriteLine();
    }
}
int[,] matrix = new int[3, 4];
PrintArray(matrix);

// Теперь опишем дополнительный метод, который будет заполнять нашу матрицу случайными числами.
// Здесь всё почти так же, как с одномерными массивами. Для i указываем matr.GetLength(0), для J —
// matr.GetLength(1). Затем обращаемся к конкретному элементу на позиции «итый-житый» и пишем
// через использование генератора псевдослучайных чисел. Возьмём полуинтервал от 1 до 10.
// Напоминаю, из-за круглых скобок может показаться, что это интервал (как в математике), но у нас
// получается именно полуинтервал.
// Проверим работоспособность нашего метода. Сначала инициализируемся, убедимся, что у нас нули.
// Затем сделаем FillArray, в качестве аргумента передадим наш массив и снова распечатаем. А чтобы
// отделить нули от чисел, перед финальной распечаткой добавим Console.WriteLine().


void FillArray(int[,] matr)
{
    for (int i = 0; i < matr.GetLength(0); i++)
    {
        for (int j = 0; j < matr.GetLength(1); j++)
        {
            matr[i, j] = new Random().Next(1, 10);//[1; 10)
        }
    }
}

PrintArray(matrix);
FillArray(matrix);
Console.WriteLine();
PrintArray(matrix);
