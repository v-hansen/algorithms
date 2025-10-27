use std::collections::hash_map::DefaultHasher;
use std::hash::{Hash, Hasher};

struct HashTable {
    buckets: Vec<Vec<(String, i32)>>,
    size: usize,
}

impl HashTable {
    fn new(size: usize) -> Self {
        HashTable {
            buckets: vec![Vec::new(); size],
            size,
        }
    }
    
    fn hash(&self, key: &str) -> usize {
        let mut hasher = DefaultHasher::new();
        key.hash(&mut hasher);
        (hasher.finish() as usize) % self.size
    }
    
    fn put(&mut self, key: String, value: i32) {
        let index = self.hash(&key);
        let bucket = &mut self.buckets[index];
        
        if let Some(pos) = bucket.iter().position(|(k, _)| k == &key) {
            bucket[pos] = (key, value);
        } else {
            bucket.push((key, value));
        }
    }
    
    fn get(&self, key: &str) -> Option<i32> {
        let index = self.hash(key);
        self.buckets[index].iter()
            .find(|(k, _)| k == key)
            .map(|(_, v)| *v)
    }
}

fn main() {
    let mut ht = HashTable::new(10);
    ht.put("key1".to_string(), 100);
    println!("{:?}", ht.get("key1"));
}