// Напишите программу, которая принимает на вход трёхзначное число и на выходе показывает вторую цифру этого числа.
// 456 -> 5
// 782 -> 8
// 918 -> 1


Console.Write("Введите трех значное число: ");
int numb1 = Convert.ToInt32(Console.ReadLine());

int third = numb1 / 100;
int second = numb1 / 10 % 10;


Console.WriteLine($"Искомое число {second}");


