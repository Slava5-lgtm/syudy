// Напишите программу, которая принимает на вход три числа и выдаёт максимальное из этих чисел.
// 2, 3, 7 -> 7
// 44 5 78 -> 78
// 22 3 9 -> 22

Console.Write("Введите целое число: ");
int numbera = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите целое число: ");
int numberb = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите целое число: ");
int numberc = Convert.ToInt32(Console.ReadLine());
// int max = numberA;
// if(numberB > max) max = numberB;
// if(numberC > max) max = numberC;
//Console.WriteLine(max);
if (a > b && a > c)
{
   System.Console.WriteLine(a);
}
else if (b > c)
{
    System.Console.WriteLine(b);
}
else System.Console.WriteLine(c);