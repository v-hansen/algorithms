class HashTable(private val size: Int = 10) {
    private val buckets = Array(size) { mutableListOf<Pair<String, Int>>() }
    
    private fun hash(key: String): Int = key.hashCode() and Int.MAX_VALUE % size
    
    fun put(key: String, value: Int) {
        val index = hash(key)
        val bucket = buckets[index]
        
        val existing = bucket.find { it.first == key }
        if (existing != null) {
            bucket.remove(existing)
        }
        bucket.add(Pair(key, value))
    }
    
    fun get(key: String): Int? {
        val index = hash(key)
        return buckets[index].find { it.first == key }?.second
    }
}

fun main() {
    val ht = HashTable()
    ht.put("key1", 100)
    println(ht.get("key1"))
}