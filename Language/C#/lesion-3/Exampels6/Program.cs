


































































































// //=====Работа с текстом=======
// // Дан текст. В тексте нужно все пробелы заменить чёрточками,
// // маленькие буквы “к” заменить большими “К”,
// // а большие “С” маленькими “с”.

// // Ясна ли задача?

// string text = " — Я думаю, — сказал князь, улыбаясь, — что,"
//             + " ежели бы вас послали вместо нашего милого Винценгероде,"
//             + " вы бы взяли приступом согласие прусского короля."
//             + " Вы так красноречивы. Вы дадите мне чаю?";


// // string s = "qwerty"
// //             0123 r - 3 позиция
// //s[3] // r

// string Replace (string text, char oldValue, newValue) // название, (входной текст, конкретный символ с
//                         //  кокого будем, на какой)
// {
//     string result = String.Empty;                   // заводим новую строку = пустая

//     int length = text.Length;
//     for (int i = 0; i < length; i++)
//     {
//         if (text[i] == oldValue) result = result + $"{newValue}";
//         else result = result + $"{text[i]}";
//     }

    

//     return result;                                  // вернуть результат
// }

// string newText = Replace(text, ' ', '|');
// Console.WritLine(newText);
// Console.WritLine();
// newText = Replace(text, 'k', 'K');
// Console.WritLine();
// newText = Replace(text, 'c', 'C');