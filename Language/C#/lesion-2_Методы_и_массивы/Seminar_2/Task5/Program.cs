// Напишите программу, которая будет принимать навход два числа и выводить, является ли первое число
//                     кратным второму. Если число 1 не кратно числу 2, то
//                     программа выводит остаток от деления.
//                     34, 5 -> не кратно, остаток 4
//                     16, 4 -> кратно

Console.Write("Введите первое число: ");
int numb1 = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите второе число: ");
int numb2 = Convert.ToInt32(Console.ReadLine());

int result = numb1 % numb2;
if(result == 0)Console.WriteLine($"Число {numb1} кратно числу {numb2} ");
else Console. WriteLine($"Число {numb1} не кратно числу {numb2}. Остаток от деления:{result}");
