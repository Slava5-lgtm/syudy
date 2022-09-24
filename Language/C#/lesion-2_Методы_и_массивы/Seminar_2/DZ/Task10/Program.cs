// Напишите программу, которая принимает на вход трёхзначное число и на выходе показывает вторую цифру этого числа.
// 456 -> 5
// 782 -> 8
// 918 -> 1


int number = new Random().Next(100, 1000);
Console.WriteLine($"Случайное число из отрезка: {number}");
// метод
int Doub(int num)
{
    
  
    int third = number / 100;
    int second = number / 10  % 10;
   return second;
}
int result = Doub(number);
Console.WriteLine($"Искомое число {result}");


