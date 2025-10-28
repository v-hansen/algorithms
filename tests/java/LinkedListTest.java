public class LinkedListTest {
    public static void main(String[] args) {
        LinkedList ll = new LinkedList();
        ll.append(1);
        ll.append(2);
        ll.append(3);
        assert ll.head.data == 1 : "Linked list failed";
        System.out.println("LinkedListTest passed");
    }
}
