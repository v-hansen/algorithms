import java.util.*;

public class KMPTest {
    public static void main(String[] args) {
        List<Integer> result = KmpAlgorithm.kmpSearch("ABABDABACDABABCABAB", "ABABCABAB");
        assert result.contains(10) : "KMP failed";
        System.out.println("KMPTest passed");
    }
}
