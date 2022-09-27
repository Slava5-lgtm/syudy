// Задача 20: Напишите программу, которая
// принимает на вход координаты двух точек и
// находит расстояние между ними в 2D
// пространстве.
// A (3,6); B (2,1) -> 5,09
// A (7,-5); B (1,-1) -> 7,21

// double num = 3.09987565;                                        // Ввели чесло
// double numRound = Math.Round(num, 2, MidpointRounding.ToZero);  // этим оператором - стратгией округлением 
//                                                                 //(MidpointRounding.ToZero) округляем до 0,01
// Console.WriteLine(numRound);            
//                                                                 //   Вывод результата

Console.WriteLine("Введите координаты точки");
Console.Write("X: ");
int numAX = Convert.ToInt32(Console.ReadLine());
Console.Write("Y: ");
int numAY = Convert.ToInt32(Console.ReadLine());

Console.WriteLine("Введите координаты точки");
Console.Write("X: ");
int numBX = Convert.ToInt32(Console.ReadLine());
Console.Write("Y: ");
int numBY = Convert.ToInt32(Console.ReadLine());

double LenghtLine (int ax, int ay, int bx, int by)
{
    if (ay == by && ax == bx) return 0;
    int x = bx - ax;
    int y = by - ay;
    return Math.Sqrt(x*x + y*y);
}

double lenghtAB = LenghtLine(numAX,numAY,numBX,numBY);
double lenght = Math.Round(lenghtAB, 2, MidpointRounding.ToZero);
Console.WriteLine($"A ({numAX}) -> {lenght}");