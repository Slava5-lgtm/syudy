// Напишите программу, которая будет выдавать название дня недели по заданному номеру.
// 3 -> Среда 5 -> Пятница
Console.WriteLine("Введите число от 1 до 7");
int num = Convert.ToInt32(Console.ReadLine());
if (num > 7)
{
    Console.WriteLine("Вы вели не колректное значение :( ");
}
if (num == 1)
{
    Console.Write("Это понидельник");
}
else if (num == 2)
{
    Console.Write("Это вторник ");
}
else if (num == 3)
{
    Console.Write("Это среда");
}
else if (num == 4)
{
    Console.Write("Это четверг");
}
else if (num == 5)
{
    Console.Write("Это пятница");
}
else if (num == 6)
{
    Console.Write("Это суббота");
}
else if (num == 7)
{
    Console.Write("Это воскрисенья");
}