class HashTable
  def initialize(size = 10)
    @size = size
    @buckets = Array.new(size) { [] }
  end
  
  def hash(key)
    key.hash % @size
  end
  
  def put(key, value)
    index = hash(key)
    @buckets[index].reject! { |k, v| k == key }
    @buckets[index] << [key, value]
  end
  
  def get(key)
    index = hash(key)
    pair = @buckets[index].find { |k, v| k == key }
    pair ? pair[1] : nil
  end
end

ht = HashTable.new
ht.put("key1", "value1")
puts ht.get("key1")