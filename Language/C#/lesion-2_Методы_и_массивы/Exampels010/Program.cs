// Взять метод передать в него массив и заполнить его нужным количеством элементов

void FillArray(int[] collection)
{
    int length = collection.Length;
    int index = 0;
    while (index < length)
    {
        collection[index] = new Random().Next(1, 10);
        // index = index + 1;
        index++;
    }
}
void PrintArray(int[] col)
{
    int count = col.Length;
    int position = 0;
    while (position < count)

    {
        Console.WriteLine(col[position]);
        position++;
    }
}
int[] array = new int[10]; // new int[x] - создай новый массив в котором будет (х) элементов

FillArray(array); // метод заполнения массива
PrintArray(array); // будет распечатовать наш массив