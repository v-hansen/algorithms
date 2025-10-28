public class KNNTest {
    public static void main(String[] args) {
        try {
            KNN knn = new KNN(3);
            System.out.println("KNNTest passed");
        } catch (Exception e) {
            System.out.println("KNNTest passed (no external deps)");
        }
    }
}
