// 17. Напишите программу,
// 1. которая принимает на вход координаты точки (X и Y),
// 2. причём X ≠ 0 и Y ≠ 0 и
// 3. выдаёт номер четверти плоскости, в которой находится эта
// точка.

Console.WriteLine("Введите координаты точки ");
Console.Write("x: ");
int x = Convert.ToInt32(Console.ReadLine());
Console.Write("y: ");
int y = Convert.ToInt32(Console.ReadLine());

int quarter = Quarter(x, y);        // вызываем метод и передаем аргументы(x, y)
string result = quarter > 0 ? $"Указаные координаты соотвествуют четверти -> {quarter.ToString()}"
                            : "Введены некоректные координаты";
Console.WriteLine(result);

int Quarter (int xc, int yc)        //(int xc, int yc) - это параметры
{
    if(xc > 0 && yc > 0) return 1; // если х > 0  &&(читаеться как (и)) y > 0 то это 1 четверть
    if(xc < 0 && yc > 0) return 2;
    if(xc < 0 && yc < 0) return 3;
    if(xc > 0 && yc < 0) return 4;
    return 0;                      // введены не коректные даные return прекрашяет работу
}