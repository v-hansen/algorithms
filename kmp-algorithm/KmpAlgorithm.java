import java.util.*;

public class KmpAlgorithm {
    
    public static int[] computeLPS(String pattern) {
        int m = pattern.length();
        int[] lps = new int[m];
        int length = 0;
        int i = 1;
        
        while (i < m) {
            if (pattern.charAt(i) == pattern.charAt(length)) {
                length++;
                lps[i] = length;
                i++;
            } else {
                if (length != 0) {
                    length = lps[length - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }
        return lps;
    }
    
    public static List<Integer> kmpSearch(String text, String pattern) {
        int n = text.length();
        int m = pattern.length();
        
        if (m == 0) return new ArrayList<>();
        
        int[] lps = computeLPS(pattern);
        List<Integer> matches = new ArrayList<>();
        
        int i = 0, j = 0;
        while (i < n) {
            if (pattern.charAt(j) == text.charAt(i)) {
                i++;
                j++;
            }
            
            if (j == m) {
                matches.add(i - j);
                j = lps[j - 1];
            } else if (i < n && pattern.charAt(j) != text.charAt(i)) {
                if (j != 0) {
                    j = lps[j - 1];
                } else {
                    i++;
                }
            }
        }
        
        return matches;
    }
    
    public static void main(String[] args) {
        String text = "ABABDABACDABABCABCABCABCABC";
        String pattern = "ABABCABCABCABC";
        List<Integer> matches = kmpSearch(text, pattern);
        System.out.println("Pattern found at indices: " + matches); // [15]
    }
}
