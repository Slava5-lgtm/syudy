// Задача 22: Напишите программу, которая
// принимает на вход число (N) и выдаёт таблицу
// квадратов чисел от 1 до N.
// 5 -> 1, 4, 9, 16, 25.
// 2 -> 1,4


void Tablesqr(int arg)
{
    int i = 1;
    if (arg > 0)
    {
        while (i <= arg)
        {
            Console.WriteLine($"{i,3} {Math.Pow((i), 2),3}");
            i++;
        }
    }
    else
    {
        Console.WriteLine("Вы ввели отрицательное значение");
    }
}


Console.WriteLine("Ведите число: ");
int num = Convert.ToInt32(Console.ReadLine());
Tablesqr(num);

