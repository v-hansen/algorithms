public class BSTTest {
    public static void main(String[] args) {
        BST bst = new BST();
        bst.insert(50);
        bst.insert(30);
        bst.insert(70);
        assert bst.search(30) == true : "BST search failed";
        assert bst.search(100) == false : "BST search failed";
        System.out.println("BSTTest passed");
    }
}
