//Вывести квадрат числа
//Ввести число
//умножить число на само себя
//Вывести результат


using System;
namespace скорость_вычислений_квадрата_числа
{
    class Program
    {
        public static void Main()
        {
            int N = 2000000000;
            double x = 2;
            // Старт 1
            var dt = DateTime.Now;
            var tm = dt.Minute;
            var ts = dt.Second;
            // Старт 1
            var t = tm * 60 + ts;    
            for (int j=0; j < N; j++)
               x = Math.Pow(x,2.0);
            dt = DateTime.Now;
            tm = dt.Minute;
            ts = dt.Second;
            // Финиш 1
            t = tm * 60 + ts - t;
            Console.WriteLine("Через Pow(), секунд - " + t);
            // Старт 2
            dt = DateTime.Now;
            tm = dt.Minute;
            ts = dt.Second;
            t = tm * 60 + ts;
            for (int j = 0; j < N; j++)
                x = x * x;
            dt = DateTime.Now;
            tm = dt.Minute;
            ts = dt.Second;
            // Финиш 2
            t = tm * 60 + ts - t;
            Console.WriteLine("Перемножение, секунд - " + t);
            Console.ReadLine();
        }
    }
}