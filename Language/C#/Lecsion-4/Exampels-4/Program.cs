﻿//                                  Рекурсия

// Здесь для вас открылась новая сущность — ситуация, при которой метод вызывает сам себя. В
// математике (программирование — это частный случай математики) есть целая область, которая
// занимается подобными случаями — рекуррентные соотношения. В программировании это просто
// называется рекурсией.
// Что такое рекурсия? Это функция, которая вызывает сама себя. Есть шутка: чтобы понять рекурсию,
// нужно понять рекурсию. В ней подчёркивается суть явления. Пример с закраской картинки непростой,
// поэтому давайте рассмотрим более тривиальный. Начнём с классической задачи математики —
// вычисления факториала. В программировании решим её с помощью рекурсии. 


//                                      Вычисление факториала

// Что такое факториал? В математике под факториалом понимают произведения чисел от 1 до
// заданного числа и обозначают его восклицательным знаком — «!». Пример факториала: 5! = 5 * 4 * 3 * 2 * 1.
// Если бы нам нужно было вычислить 120!, мы бы считали произведение чисел от 1 до 120.
// Программисты выяснили, что если мы считаем 5 * на произведение чисел от 1 до 4, по определению
// факториала, это 4!. Таким образом, 5! мы можем представить как 5 * 4!. 4! — это 4 * 3! и так далее.
// Таким образом, мы смогли задать функцию через саму себя. Попробуем написать это кодом.
// Определим функцию или метод, который будет принимать число, факториал которого нужно
// вычислить. Как вы понимаете, это снова метод, который принимает какой-то аргумент (в частности,
// число) и возвращает факториал этого числа.
// Определим метод как возвращающий int, и в качестве аргумента принимающий другое целое число.
// Далее по определению факториала мы явно укажем: «если мы дошли до единицы (n = 1), мы должны
// вернуть 1». Почему? Это определение факториала: 1! = 1.Кстати, отметим, что 0! — это тоже 1.
// Итак, если n = 1, возвращаем 1. В противном случае берём текущее значение и умножаем на факториал
// предыдущего числа (n - 1). Не забываем, что мы должны явно возвращать значение. То есть, если 1,
// возвращаем 1. Если не 1, то n * Factorial(n-1) (факториал предыдущего числа).

// int Factorial(int n)
// {
//     // 1! = 1
//     // 0! = 1
//     if (n == 1) return 1;
//     else return n * Factorial(n - 1);
// }
// Console.WriteLine(Factorial(40)); // 1 * 2 * 3 = 6



// Казалось бы, задачу решили. Но есть проблема: когда мы будем вычислять большие числа (допустим,
// 40!), в какой-то момент начнём получать отрицательные числа, чего быть не должно. 

// int Factorial(int n)
// {
//     // 1! = 1
//     // 0! = 1
//     if (n == 1) return 1;
//     else return n * Factorial(n - 1);
// }
// for (int i = 1; i < 40; i++)
// {
//     Console.WriteLine(Factorial(i));
// }


// Это связано с переполнением типа. Давайте проверим, до какого значения можем посчитать
// факториал.

// int Factorial(int n)
// {
//     // 1! = 1
//     // 0! = 1
//     if (n == 1) return 1;
//     else return n * Factorial(n - 1);
// }
// for (int i = 1; i < 40; i++)
// {
//     Console.WriteLine($"{i}! = {Factorial(i)}");
// }
//Очистим и запустим терминал. Всё хорошо до 17!.


// То есть число 17! попросту не вмещается в тип данных integer, поэтому появляется первая ваша задача,
// связанная с переполнением. Как её решать? Разными способами. Есть тип данных, который такие числа
// ещё способен переваривать, — double. Давайте integer заменим на double для возвращаемого
// результата. Потому что аргументом мы здесь передаём только число до 40.

double Factorial(int n)
{
    // 1! = 1
    // 0! = 1
    if (n == 1) return 1;
    else return n * Factorial(n - 1);
}
for (int i = 1; i < 40; i++)
{
    Console.WriteLine($"{i}! = {Factorial(i)}");
}

// Видим нормальные значения. E + 29 означает, что получившееся число нужно умножить на 10 в 29 степени.
// Это достаточно большие числа. Но тип double позволяет их хранить. 