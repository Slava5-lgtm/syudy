//Сравнение цифр

int a = 2;
int b = 5;
int c = 34;

// int max = a;
// if(b > max) max = b;
// if (c > max) max = c;
// System.Console.WriteLine(max);
if (a > b && a > c)
{
   System.Console.WriteLine(a);
}
else if (b > c)
{
    System.Console.WriteLine(b);
}
else System.Console.WriteLine(c);
