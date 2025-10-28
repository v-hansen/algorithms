public class MatrixMultTest {
    public static void main(String[] args) {
        int[][] a = {{1, 2}, {3, 4}};
        int[][] b = {{5, 6}, {7, 8}};
        int[][] result = MatrixMultiplication.multiply(a, b);
        assert result[0][0] == 19 && result[1][1] == 50 : "Matrix mult failed";
        System.out.println("MatrixMultTest passed");
    }
}
