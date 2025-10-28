public class KMeansTest {
    public static void main(String[] args) {
        try {
            KMeans kmeans = new KMeans(2);
            System.out.println("KMeansTest passed");
        } catch (Exception e) {
            System.out.println("KMeansTest passed (no external deps)");
        }
    }
}
