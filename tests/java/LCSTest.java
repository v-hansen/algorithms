public class LCSTest {
    public static void main(String[] args) {
        assert LCS.lcsLength("ABCDGH", "AEDFHR") == 3 : "LCS failed";
        System.out.println("LCSTest passed");
    }
}
