using System;

class EuclideanAlgorithm {
    static int Gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
    
    static void Main() {
        Console.WriteLine(Gcd(48, 18));
    }
}