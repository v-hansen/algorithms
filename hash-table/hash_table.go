package main
import "fmt"

type HashTable struct {
    buckets [][]Pair
    size    int
}

type Pair struct {
    key   string
    value int
}

func NewHashTable(size int) *HashTable {
    return &HashTable{
        buckets: make([][]Pair, size),
        size:    size,
    }
}

func (ht *HashTable) hash(key string) int {
    sum := 0
    for _, c := range key {
        sum += int(c)
    }
    return sum % ht.size
}

func (ht *HashTable) Put(key string, value int) {
    index := ht.hash(key)
    bucket := &ht.buckets[index]
    
    for i, pair := range *bucket {
        if pair.key == key {
            (*bucket)[i].value = value
            return
        }
    }
    *bucket = append(*bucket, Pair{key, value})
}

func (ht *HashTable) Get(key string) int {
    index := ht.hash(key)
    for _, pair := range ht.buckets[index] {
        if pair.key == key {
            return pair.value
        }
    }
    return -1
}

func main() {
    ht := NewHashTable(10)
    ht.Put("key1", 100)
    fmt.Println(ht.Get("key1"))
}