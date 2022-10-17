// // Напишите программу, которая принимает на вход три числа и выдаёт максимальное из этих чисел.
// // 2, 3, 7 -> 7
// // 44 5 78 -> 78
// // 22 3 9 -> 22

Console.Write("Ввдите число: ");
int a = Convert.ToInt32(Console.ReadLine());
Console.Write("Ввдите число: ");
int b = Convert.ToInt32(Console.ReadLine());
Console.Write("Ввдите число: ");
int c = Convert.ToInt32(Console.ReadLine());
//int max = a;
// if (b > max) max = b;
// if (c > max) max = c;
//Console.WriteLine(max);
//Console.Write($"самое большое число {max}");
if (a > b && a > c) 

{
   System.Console.Write($"самое большое число {a}");//Line(a);
}
else if (b > c) 
{
    System.Console.Write($"самое большое число {b}");//Line(b);
}
else System.Console.Write($"самое большое число {c}");//Line(c);


