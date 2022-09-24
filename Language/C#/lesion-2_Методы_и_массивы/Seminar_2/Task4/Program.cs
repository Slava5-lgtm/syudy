// Напишите программу, которая выводит случайное
// трёхзначное число и удаляет вторую цифру этого
// числа.
// 456 -> 46
// 782 -> 72
// 918 -> 98

// int number = new Random().Next(100, 1000);
// Console.WriteLine($"Случайное число из отрезка: {number}");


// int first = number / 100;
// int third = number % 10;
// int result = first * 10 + third;

// Console.WriteLine($"Искомое число{result}");

// Через метод

int number = new Random().Next(100, 1000);
Console.WriteLine($"Случайное число из отрезка: {number}");
// метод
int Doub(int num)
{
    int first = number / 100;
    int third = number % 10;
    return  first * 10 + third;
}
int result = Doub(number);
Console.WriteLine($"Искомое число {result}");