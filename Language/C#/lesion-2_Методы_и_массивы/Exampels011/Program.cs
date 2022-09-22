//Метод который показывает позицию задоного числа

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
int IndexOF(int[] collection, int find)
{
    int count = collection.Length;
    int index = 0;
    int position = -1;
    while (index < count)
    {
        if(collection[index] == find)
        {
           position = index;
           break; 
        }
        index++;
    }
    return position;
}
int[] array = new int[10];

FillArray(array);
//array[4] = 4; // принудительно добавили позицию
PrintArray(array);
Console.WriteLine();

int pos = IndexOF(array, 4); // результат работы метода IndexOF
Console.WriteLine(pos);