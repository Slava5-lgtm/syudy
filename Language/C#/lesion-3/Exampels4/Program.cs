// МЕТОД Что возрошяют, что то принемают
string Method4(int count, string text)
{
    int i = 0;
    string result = String.Empty;
    while (i < count)
    {
        result = result + text;
        i++;
    }
    return result;
}


string res = Method4(10, "12");
Console.WriteLine(res);
// string Method4(int count, string text) - строку возврошяет мы будем строку передовать count раз
//                             Цикл
// {
//     int i = 0;
//     string result = String.Empty;      - переменая (result) куда кладем результат = пустая трока (String.Empty)
//     while (i < count)                  -  
//     {
//         result = result + text;
//         i++;
//     }
//     return result;                     -
// }


// string res = Method4(10, "12");        - вызов метода Method4 (сколько раз выводиться (10), что выводиться(12))
// Console.WriteLine(res);