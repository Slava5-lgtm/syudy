// МЕТОД 3 - Что ворощяют но нечего не возрошяют

// int Method3()                   - имя метода
// {
//     return DateTime.Now.Year;   - оператор return текущая дата
// }

// int year = Method3();           - вызов метода указываем имя метода, вводим переменую (year)
//                                 - через оператор присваевания = кладем нужное значения
// Console.WriteLine(year);        - указываем имя переменой  иполучаем то значения который вернул метод

int Method3()
{
    return DateTime.Now.Year;
}
int year = Method3();
Console.WriteLine(year);



