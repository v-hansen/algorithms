using System;

class Program {
    static bool IsPalindrome(string str) {
        str = str.ToLower();
        char[] arr = str.ToCharArray();
        Array.Reverse(arr);
        return str == new string(arr);
    }
    
    static void Main() {
        Console.WriteLine(IsPalindrome("racecar"));
        Console.WriteLine(IsPalindrome("hello"));
    }
}
