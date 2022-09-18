//Являеться первое число квадратом второго
Console.WriteLine("Введите два числа и мы узнаем являеться ли первое число квадратом второго");
Console.Write("Ввдите первое число: ");
int a = Convert.ToInt32(Console.ReadLine());
Console.Write("Ввдите второе число: ");
int b = Convert.ToInt32(Console.ReadLine());
int sqr_b = b * b;
if (sqr_b == a)
{
    Console.Write($"Да, первое число {a} - это квадрат второго числа {b}");
}
else
{
    Console.Write($"Нет, первое число {a} - это не квадрат второго чила {b}. Квадрат числа {b} - это {sqr_b}");
}