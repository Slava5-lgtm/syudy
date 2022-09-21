// Задача 9. Напишите программу, которая выводит
// 1. случайное число из отрезка [10, 99] и
// 2. показывает наибольшую цифру числа.
// 3. Вывод результата

// 78 -> 8
// 12-> 2
// 85 -> 8
int number = new Random().Next(10, 100);
System.Console.WriteLine($"Случайное число из отрезка 10 - 99 => {number}"); // без этой строки если цифры равны не будет показывать слуйчайное число
int firstDigit = number / 10;
int secondDigit = number % 10;

if (firstDigit == secondDigit) System.Console.WriteLine("Цифры одинаковые"); // == - равен, != - не равен
else if(firstDigit > secondDigit) Console.WriteLine($"Наибольшое цифра числа {number} => {firstDigit}");
else Console.WriteLine($"Наибольшое цифра числа {number} => {firstDigit}");

// int maxDigit = 0;
// if (firstDigit > secondDigit) maxDigit = firstDigit;
// else firstDigit = secondDigit;

//int max = firstDigit > secondDigit ? firstDigit : secondDigit;