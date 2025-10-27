class HashTable<T> {
    private size: number;
    private table: Array<Array<[string, T]>>;
    
    constructor(size: number = 10) {
        this.size = size;
        this.table = Array(size).fill(null).map(() => []);
    }
    
    private hash(key: string): number {
        let hash = 0;
        for (let i = 0; i < key.length; i++) {
            hash = (hash + key.charCodeAt(i) * i) % this.size;
        }
        return hash;
    }
    
    put(key: string, value: T): void {
        const index = this.hash(key);
        const bucket = this.table[index];
        
        for (let i = 0; i < bucket.length; i++) {
            if (bucket[i][0] === key) {
                bucket[i][1] = value;
                return;
            }
        }
        bucket.push([key, value]);
    }
    
    get(key: string): T {
        const index = this.hash(key);
        const bucket = this.table[index];
        
        for (const [k, v] of bucket) {
            if (k === key) return v;
        }
        throw new Error(`Key ${key} not found`);
    }
}

const ht = new HashTable<any>();
ht.put("name", "Alice");
ht.put("age", 30);
console.log(ht.get("name")); // Alice
