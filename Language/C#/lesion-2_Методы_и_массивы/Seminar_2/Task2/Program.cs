// Задача 9. Напишите программу, которая выводит
// 1. случайное число из отрезка [10, 99] и
// 2. показывает наибольшую цифру числа.
// 3. Вывод результата

// 78 -> 8
// 12-> 2
// 85 -> 8

int number = new Random().Next(10, 100);
Console.WriteLine($"Случайное число из отрезка 10 - 99 => {number}");

int MaxDigit (int num)
{
    int firstDigit = number / 10;
    int secondDigit = number % 10;
    if(firstDigit == secondDigit) return -1;
    return firstDigit > secondDigit ? firstDigit : secondDigit;
}

// метод сравнивания двух цифр
bool isEqualDigits(int num1, int num2) 
{
    return num1 == num2;
}


int maxDigit = MaxDigit(number);
string result = maxDigit != -1 ? maxDigit.ToString(): "цифры одинаковы";
Console.WriteLine($"Наибольшое цифра числа {number} => {result}");

