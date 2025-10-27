public class Palindrome {
    public static boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
    
    public static boolean isPalindromeClean(String s) {
        StringBuilder cleaned = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                cleaned.append(Character.toLowerCase(c));
            }
        }
        String str = cleaned.toString();
        return isPalindrome(str);
    }
    
    public static boolean isPalindromeRecursive(String s, int left, int right) {
        if (left >= right) return true;
        if (s.charAt(left) != s.charAt(right)) return false;
        return isPalindromeRecursive(s, left + 1, right - 1);
    }
    
    public static void main(String[] args) {
        System.out.println(isPalindrome("racecar"));
        System.out.println(isPalindromeClean("A man, a plan, a canal: Panama"));
        System.out.println(isPalindromeRecursive("level", 0, 4));
    }
}