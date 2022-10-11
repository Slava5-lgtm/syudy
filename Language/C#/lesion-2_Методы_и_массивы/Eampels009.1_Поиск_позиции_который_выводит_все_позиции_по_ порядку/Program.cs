void FillArray(int[] collection)    //  FillArray - имя метода   

{
    int length = collection.Length; //  collection.Length - длина массива
    int index = 0;
    while (index < length)
    {
        collection[index] = new Random().Next(1, 10);
        //index = index + 1;
        index++;
    } 
}

void PrintArray(int[] col)      //  Теперь сделаем метод void, который будет печатать массив.
                                //  Аналогичным образом в качестве аргумента здесь будет приходить
                                //  массив. Обратите внимание, что здесь мы специально не
                                // даём одинаковые имена, чтобы привыкнуть называть разные
                                //  аргументы различными именами. То есть в первом случае будет
                                //collection, а во втором, например, col:
{
    int count = col.Length;     //  Количество элементов
    int position = 0;           //  Далее обозначим текущую позицию не через именование перемен
                                //  index, а через position
    while (position < count)    //  Возмем новый цикл
    {
        Console.WriteLine(col[position]);   //  Затем выведем через Console.WriteLine значение
                                            // текущего элемента, то есть col[position]
        position++;                         //  То есть увеличиваем значение текущей позиции
    }
}



int[] array = new int[10];      // укажем, что в этом массиве будет по умолчанию 10 элементов
                                //new int[10]

FillArray(array);
array[4] = 4;
array[6] = 4;
PrintArray(array);
Console.WriteLine();
Console.WriteLine(array);

//  для чего используется ключевое слово void. Дело в том, что в контексте языка С# есть методы, которые могут возвращать или
//  не возвращать какие-то значения. Если метод ничего не возвращает, он называется void-методом.