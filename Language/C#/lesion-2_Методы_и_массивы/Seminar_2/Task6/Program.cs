// Напишите программу, которая принимает на вход число и проверяет, кратно ли оно одновременно 7 и 23.
// 14 -> нет
// 46 -> нет
// 161 -> да  

int checkMultiple(int check_arg, int divarg1, int divarg2)
{
    int result = 1;
    if(check_arg % divarg1 == 0 && check_arg % divarg2 == 0) result = 0;
    return result;
}

Console.Write("Введите число кратность которого мы будем проверять; "); // запросили первое число
int numCheck = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите первое число на кратность которого мы будем проверять; "); // запросили первое число
int fistNum = Convert.ToInt32(Console.ReadLine()); // перевили строку в цифры
Console.Write("Введите второе число на кратность которого мы будем проверять; "); // запросили второе число
int secondNum = Convert.ToInt32(Console.ReadLine());
int resultMehod = checkMultiple(numCheck, fistNum, secondNum);
if (resultMehod == 0)
{
    Console.Write("да");
}
else
{
    Console.Write("нет");
}