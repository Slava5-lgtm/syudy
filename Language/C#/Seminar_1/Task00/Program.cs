// 0.Демонстпация решения
// Напишите програму, которая на входе 
// принемает число ((на входе принемает число) - число вводит пользователь))
// и выдает его квадрат (число умноженое само на себя)

// решаем по пунктам
// 1. на вход получит число
// 2. выдает его квадрат
// 3. Вывод результата
// 4 -> 16
// -3 -> 9
// -7 -> 49

// Console.ReadLine - то что вводит пользовател этой комадой это строка
Console.Write("Введите целое число: "); // Console.Write - команда для пользователя
int number = Convert.ToInt32(Console.ReadLine()); //number - имя переменой. Convert.To(Int32, Double) - преобразовываем string(строку) в int (целое число)
// double number = Convert.ToDouble(Console.ReadLine()); Convert.ToDouble - преобразовываем string(строку) в Double (количественое) 
// string str1 = Console.ReadLine(); преоброзования не делаем
int square = number * number;
//Console.WriteLine("Квадрат числа {number} = {square}");  // буз $ - будет просто текст
Console.WriteLine($"Квадрат числа {number} = {square}"); // $ - этот символ выводит переменые (цифры)