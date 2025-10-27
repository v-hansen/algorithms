#!/usr/bin/env python3
import os

def complete_binary_search_tree():
    """Completa BST implementações pequenas"""
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/binary-search-tree"
    
    # Kotlin
    with open(f"{base_dir}/BinarySearchTree.kt", "w") as f:
        f.write("""class Node(var data: Int) {
    var left: Node? = null
    var right: Node? = null
}

class BST {
    private var root: Node? = null
    
    fun insert(data: Int) {
        root = insertRec(root, data)
    }
    
    private fun insertRec(root: Node?, data: Int): Node {
        if (root == null) return Node(data)
        
        if (data < root.data) root.left = insertRec(root.left, data)
        else root.right = insertRec(root.right, data)
        
        return root
    }
    
    fun search(data: Int): Boolean = searchRec(root, data)
    
    private fun searchRec(root: Node?, data: Int): Boolean {
        if (root == null) return false
        if (root.data == data) return true
        return if (data < root.data) searchRec(root.left, data) else searchRec(root.right, data)
    }
}

fun main() {
    val bst = BST()
    listOf(50, 30, 70, 20, 40).forEach { bst.insert(it) }
    println(bst.search(40))
}""")

    # Rust
    with open(f"{base_dir}/binary_search_tree.rs", "w") as f:
        f.write("""use std::rc::Rc;
use std::cell::RefCell;

type NodeRef = Rc<RefCell<Node>>;

struct Node {
    data: i32,
    left: Option<NodeRef>,
    right: Option<NodeRef>,
}

struct BST {
    root: Option<NodeRef>,
}

impl BST {
    fn new() -> Self {
        BST { root: None }
    }
    
    fn insert(&mut self, data: i32) {
        self.root = Self::insert_rec(self.root.take(), data);
    }
    
    fn insert_rec(node: Option<NodeRef>, data: i32) -> Option<NodeRef> {
        match node {
            None => Some(Rc::new(RefCell::new(Node {
                data,
                left: None,
                right: None,
            }))),
            Some(n) => {
                if data < n.borrow().data {
                    n.borrow_mut().left = Self::insert_rec(n.borrow_mut().left.take(), data);
                } else {
                    n.borrow_mut().right = Self::insert_rec(n.borrow_mut().right.take(), data);
                }
                Some(n)
            }
        }
    }
    
    fn search(&self, data: i32) -> bool {
        Self::search_rec(&self.root, data)
    }
    
    fn search_rec(node: &Option<NodeRef>, data: i32) -> bool {
        match node {
            None => false,
            Some(n) => {
                let node_data = n.borrow().data;
                if node_data == data {
                    true
                } else if data < node_data {
                    Self::search_rec(&n.borrow().left, data)
                } else {
                    Self::search_rec(&n.borrow().right, data)
                }
            }
        }
    }
}

fn main() {
    let mut bst = BST::new();
    for val in [50, 30, 70, 20, 40] {
        bst.insert(val);
    }
    println!("{}", bst.search(40));
}""")

    # TypeScript
    with open(f"{base_dir}/binary_search_tree.ts", "w") as f:
        f.write("""class TreeNode {
    data: number;
    left: TreeNode | null = null;
    right: TreeNode | null = null;
    
    constructor(data: number) {
        this.data = data;
    }
}

class BST {
    private root: TreeNode | null = null;
    
    insert(data: number): void {
        this.root = this.insertRec(this.root, data);
    }
    
    private insertRec(node: TreeNode | null, data: number): TreeNode {
        if (!node) return new TreeNode(data);
        
        if (data < node.data) node.left = this.insertRec(node.left, data);
        else node.right = this.insertRec(node.right, data);
        
        return node;
    }
    
    search(data: number): boolean {
        return this.searchRec(this.root, data);
    }
    
    private searchRec(node: TreeNode | null, data: number): boolean {
        if (!node) return false;
        if (node.data === data) return true;
        return data < node.data ? this.searchRec(node.left, data) : this.searchRec(node.right, data);
    }
}

const bst = new BST();
[50, 30, 70, 20, 40].forEach(x => bst.insert(x));
console.log(bst.search(40));""")

def complete_hash_table():
    """Completa Hash Table implementações pequenas"""
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/hash-table"
    
    # Kotlin
    with open(f"{base_dir}/HashTable.kt", "w") as f:
        f.write("""class HashTable(private val size: Int = 10) {
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
}""")

    # Rust
    with open(f"{base_dir}/hash_table.rs", "w") as f:
        f.write("""use std::collections::hash_map::DefaultHasher;
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
}""")

def complete_dijkstra():
    """Completa Dijkstra implementações pequenas"""
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/dijkstra-algorithm"
    
    # C
    with open(f"{base_dir}/dijkstra_algorithm.c", "w") as f:
        f.write("""#include <stdio.h>
#include <limits.h>
#include <stdbool.h>

#define V 4

int minDistance(int dist[], bool sptSet[]) {
    int min = INT_MAX, min_index;
    for (int v = 0; v < V; v++)
        if (!sptSet[v] && dist[v] <= min)
            min = dist[v], min_index = v;
    return min_index;
}

void dijkstra(int graph[V][V], int src) {
    int dist[V];
    bool sptSet[V];
    
    for (int i = 0; i < V; i++)
        dist[i] = INT_MAX, sptSet[i] = false;
    
    dist[src] = 0;
    
    for (int count = 0; count < V - 1; count++) {
        int u = minDistance(dist, sptSet);
        sptSet[u] = true;
        
        for (int v = 0; v < V; v++)
            if (!sptSet[v] && graph[u][v] && dist[u] != INT_MAX && dist[u] + graph[u][v] < dist[v])
                dist[v] = dist[u] + graph[u][v];
    }
    
    for (int i = 0; i < V; i++)
        printf("%d: %d\\n", i, dist[i]);
}

int main() {
    int graph[V][V] = {{0, 1, 4, 0}, {1, 0, 2, 5}, {4, 2, 0, 1}, {0, 5, 1, 0}};
    dijkstra(graph, 0);
    return 0;
}""")

    # Go
    with open(f"{base_dir}/dijkstra_algorithm.go", "w") as f:
        f.write("""package main
import (
    "fmt"
    "math"
)

func dijkstra(graph [][]int, src int) []int {
    V := len(graph)
    dist := make([]int, V)
    sptSet := make([]bool, V)
    
    for i := 0; i < V; i++ {
        dist[i] = math.MaxInt32
    }
    dist[src] = 0
    
    for count := 0; count < V-1; count++ {
        u := minDistance(dist, sptSet)
        sptSet[u] = true
        
        for v := 0; v < V; v++ {
            if !sptSet[v] && graph[u][v] != 0 && dist[u] != math.MaxInt32 && dist[u]+graph[u][v] < dist[v] {
                dist[v] = dist[u] + graph[u][v]
            }
        }
    }
    
    return dist
}

func minDistance(dist []int, sptSet []bool) int {
    min := math.MaxInt32
    minIndex := 0
    
    for v := 0; v < len(dist); v++ {
        if !sptSet[v] && dist[v] <= min {
            min = dist[v]
            minIndex = v
        }
    }
    
    return minIndex
}

func main() {
    graph := [][]int{
        {0, 1, 4, 0},
        {1, 0, 2, 5},
        {4, 2, 0, 1},
        {0, 5, 1, 0},
    }
    
    result := dijkstra(graph, 0)
    for i, d := range result {
        fmt.Printf("%d: %d\\n", i, d)
    }
}""")

    # TypeScript
    with open(f"{base_dir}/dijkstra_algorithm.ts", "w") as f:
        f.write("""function dijkstra(graph: number[][], src: number): number[] {
    const V = graph.length;
    const dist = new Array(V).fill(Infinity);
    const sptSet = new Array(V).fill(false);
    
    dist[src] = 0;
    
    for (let count = 0; count < V - 1; count++) {
        const u = minDistance(dist, sptSet);
        sptSet[u] = true;
        
        for (let v = 0; v < V; v++) {
            if (!sptSet[v] && graph[u][v] && dist[u] !== Infinity && dist[u] + graph[u][v] < dist[v]) {
                dist[v] = dist[u] + graph[u][v];
            }
        }
    }
    
    return dist;
}

function minDistance(dist: number[], sptSet: boolean[]): number {
    let min = Infinity;
    let minIndex = 0;
    
    for (let v = 0; v < dist.length; v++) {
        if (!sptSet[v] && dist[v] <= min) {
            min = dist[v];
            minIndex = v;
        }
    }
    
    return minIndex;
}

const graph = [
    [0, 1, 4, 0],
    [1, 0, 2, 5],
    [4, 2, 0, 1],
    [0, 5, 1, 0]
];

const result = dijkstra(graph, 0);
result.forEach((d, i) => console.log(`${i}: ${d}`));""")

if __name__ == "__main__":
    print("Completando implementações faltantes...")
    complete_binary_search_tree()
    complete_hash_table()
    complete_dijkstra()
    print("Primeira fase completada!")
