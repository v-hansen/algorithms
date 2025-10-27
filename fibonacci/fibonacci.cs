using System;

class Program
{
    static int Fibonacci(int n)
    {
        if (n <= 1) return n;
        return Fibonacci(n - 1) + Fibonacci(n - 2);
    }

    static void Main()
    {
        Console.WriteLine(Fibonacci(10));
    }
}
