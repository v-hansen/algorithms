public class PalindromeTest {
    public static void main(String[] args) {
        assert Palindrome.isPalindromeSimple("racecar") == true : "Palindrome failed";
        assert Palindrome.isPalindromeSimple("hello") == false : "Palindrome failed";
        System.out.println("PalindromeTest passed");
    }
}
