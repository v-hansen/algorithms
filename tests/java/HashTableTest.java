public class HashTableTest {
    public static void main(String[] args) {
        HashTable ht = new HashTable();
        ht.put("key1", "value1");
        ht.put("key2", "value2");
        assert ht.get("key1").equals("value1") : "Hash table failed";
        System.out.println("HashTableTest passed");
    }
}
