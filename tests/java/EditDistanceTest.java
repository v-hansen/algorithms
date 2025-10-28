public class EditDistanceTest {
    public static void main(String[] args) {
        assert EditDistance.editDistance("kitten", "sitting") == 3 : "Edit distance failed";
        System.out.println("EditDistanceTest passed");
    }
}
