class HashTable {
    constructor(size = 10) {
        this.size = size;
        this.table = Array(size).fill(null).map(() => []);
    }
    
    _hash(key) {
        let hash = 0;
        for (let i = 0; i < key.length; i++) {
            hash = (hash + key.charCodeAt(i) * i) % this.size;
        }
        return hash;
    }
    
    put(key, value) {
        const index = this._hash(key);
        const bucket = this.table[index];
        
        for (let i = 0; i < bucket.length; i++) {
            if (bucket[i][0] === key) {
                bucket[i][1] = value;
                return;
            }
        }
        bucket.push([key, value]);
    }
    
    get(key) {
        const index = this._hash(key);
        const bucket = this.table[index];
        
        for (const [k, v] of bucket) {
            if (k === key) return v;
        }
        throw new Error(`Key ${key} not found`);
    }
}

const ht = new HashTable();
ht.put("name", "Alice");
ht.put("age", 30);
console.log(ht.get("name")); // Alice
