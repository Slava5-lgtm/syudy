// Задача 18: Напишите программу, которая по
// заданному номеру четверти, показывает диапазон
// возможных координат точек в этой четверти (x и y).

Console.WriteLine("Введите номер четверти");
int quarterNum = Convert.ToInt32(Console.ReadLine());

string FindRange(int num)
{
    if(num ==1) return "Деапозон координат находиться в пределах x > 0 и y > 0";
    if(num ==2) return "Деапозон координат находиться в пределах x < 0 и y > 0";
    if(num ==3) return "Деапозон координат находиться в пределах x < 0 и y < 0";
    if(num ==4) return "Деапозон координат находиться в пределах x < 0 и y > 0";

}
string Range = FindRange(quarterNum);
Console.WriteLine(range);