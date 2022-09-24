// Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
// 5, 25 -> да
// -4, 16 -> да
// 25, 5 -> да
// 8,9 -> нет
 
// метод void
// void checkOnSquare(int arg1,int arg2)
// {
//     int sqr = 0;
//     if (arg1 < arg2)
//     {
//     sqr = arg1 * arg1;
//     if (sqr == arg2)
//         {
//             Console.WriteLine($"Число {arg2} являеться квадратом числа {arg1}");
//         }
//         else
//         {
//             Console.WriteLine($"Число {arg2} не являеться квадратом числа {arg1}");
//         }
//     }
//     else
//     {
//         sqr = arg2 * arg2;
//         if (sqr == arg1)
//         {
//            Console.WriteLine($"Число {arg1} являеться квадратом числа {arg2}");  
//         }
//         else
//         {
//             Console.WriteLine($"Число {arg1} не являеться квадратом числа {arg2}");
//         }
        
//     }
// }


// Console.Write("Введите первое число: "); 
// int fistNum = Convert.ToInt32(Console.ReadLine());
// Console.Write("Введите второе число: "); 
// int secondNum = Convert.ToInt32(Console.ReadLine());
// checkOnSquare(fistNum, secondNum);

// метод bool

Console.Write("Введите первое число: "); 
int numA = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите второе число: "); 
int numB = Convert.ToInt32(Console.ReadLine());

bool IsPairSqure(int num1, int num2)
{
    return (num1 == num2 * num2) || (num2 == num1 * num1); 
}
if (IsPairSqure(numA, numB)) Console.WriteLine($"{numA}, {numB} -> да");
else Console.WriteLine($"{numA}, {numB} -> нет");
    
