Console.WriteLine ("Введите любо целое положительное число");

string number = Console.ReadLine();

int number1 = int.Parse (number);

int n = 1;

bool not = true;

Console.WriteLine("Чётные числа от 1 до " + number1);
            while (n <= number1)
            {
                if (n % 2 != 1)
                {
                    Console.Write(n + ", ");
                    not = false;
                }
                n++;
            }