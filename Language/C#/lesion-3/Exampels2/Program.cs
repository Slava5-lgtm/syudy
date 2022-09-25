// ВИД 2 Принемает аргумент, но нечего не возрощяет

// void Method2(string msg) // msd - аргумент
// {
//     Console.WriteLine(msg);
// }
// Method2(msg: "Текст сообшений");

void Method21(string msg, int count) // метод принемает 2 аргумента - строка и целое число
{
    int i = 0;
    while (i < count)
    {
        Console.WriteLine(msg);
        i++; // счетчик
    }
}
// Method21("Текст", 4); // вызов метода ("тест", 4-сколько раз будет показывать)
Method21(msg: "Текст", count: 4);
//Method21(count: 4, msg: "новый Текст");