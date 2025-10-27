#!/usr/bin/env python3
import os

def complete_dynamic_programming():
    """Completa DP implementações pequenas"""
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/dynamic-programming"
    
    # Kotlin
    with open(f"{base_dir}/DynamicProgramming.kt", "w") as f:
        f.write("""fun fibonacci(n: Int): Int {
    if (n <= 1) return n
    val dp = IntArray(n + 1)
    dp[0] = 0
    dp[1] = 1
    for (i in 2..n) {
        dp[i] = dp[i-1] + dp[i-2]
    }
    return dp[n]
}

fun coinChange(coins: IntArray, amount: Int): Int {
    val dp = IntArray(amount + 1) { Int.MAX_VALUE }
    dp[0] = 0
    
    for (coin in coins) {
        for (i in coin..amount) {
            if (dp[i - coin] != Int.MAX_VALUE) {
                dp[i] = minOf(dp[i], dp[i - coin] + 1)
            }
        }
    }
    
    return if (dp[amount] == Int.MAX_VALUE) -1 else dp[amount]
}

fun main() {
    println("Fibonacci(10): ${fibonacci(10)}")
    println("Coin change: ${coinChange(intArrayOf(1, 3, 4), 6)}")
}""")

    # Rust
    with open(f"{base_dir}/dynamic_programming.rs", "w") as f:
        f.write("""fn fibonacci(n: usize) -> u64 {
    if n <= 1 { return n as u64; }
    let mut dp = vec![0u64; n + 1];
    dp[1] = 1;
    for i in 2..=n {
        dp[i] = dp[i-1] + dp[i-2];
    }
    dp[n]
}

fn coin_change(coins: &[i32], amount: i32) -> i32 {
    let mut dp = vec![i32::MAX; (amount + 1) as usize];
    dp[0] = 0;
    
    for &coin in coins {
        for i in coin..=amount {
            if dp[(i - coin) as usize] != i32::MAX {
                dp[i as usize] = dp[i as usize].min(dp[(i - coin) as usize] + 1);
            }
        }
    }
    
    if dp[amount as usize] == i32::MAX { -1 } else { dp[amount as usize] }
}

fn main() {
    println!("Fibonacci(10): {}", fibonacci(10));
    println!("Coin change: {}", coin_change(&[1, 3, 4], 6));
}""")

    # TypeScript
    with open(f"{base_dir}/dynamic_programming.ts", "w") as f:
        f.write("""function fibonacci(n: number): number {
    if (n <= 1) return n;
    const dp = new Array(n + 1);
    dp[0] = 0;
    dp[1] = 1;
    for (let i = 2; i <= n; i++) {
        dp[i] = dp[i-1] + dp[i-2];
    }
    return dp[n];
}

function coinChange(coins: number[], amount: number): number {
    const dp = new Array(amount + 1).fill(Infinity);
    dp[0] = 0;
    
    for (const coin of coins) {
        for (let i = coin; i <= amount; i++) {
            dp[i] = Math.min(dp[i], dp[i - coin] + 1);
        }
    }
    
    return dp[amount] === Infinity ? -1 : dp[amount];
}

console.log("Fibonacci(10):", fibonacci(10));
console.log("Coin change:", coinChange([1, 3, 4], 6));""")

def complete_linked_list():
    """Completa Linked List implementações pequenas"""
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/linked-list"
    
    # Kotlin
    with open(f"{base_dir}/LinkedList.kt", "w") as f:
        f.write("""class Node(var data: Int) {
    var next: Node? = null
}

class LinkedList {
    private var head: Node? = null
    
    fun append(data: Int) {
        val newNode = Node(data)
        if (head == null) {
            head = newNode
            return
        }
        
        var current = head
        while (current?.next != null) {
            current = current.next
        }
        current?.next = newNode
    }
    
    fun prepend(data: Int) {
        val newNode = Node(data)
        newNode.next = head
        head = newNode
    }
    
    fun display() {
        var current = head
        while (current != null) {
            print("${current.data} -> ")
            current = current.next
        }
        println("null")
    }
    
    fun search(data: Int): Boolean {
        var current = head
        while (current != null) {
            if (current.data == data) return true
            current = current.next
        }
        return false
    }
}

fun main() {
    val list = LinkedList()
    list.append(1)
    list.append(2)
    list.prepend(0)
    list.display()
    println("Search 2: ${list.search(2)}")
}""")

    # Rust
    with open(f"{base_dir}/linked_list.rs", "w") as f:
        f.write("""struct Node {
    data: i32,
    next: Option<Box<Node>>,
}

struct LinkedList {
    head: Option<Box<Node>>,
}

impl LinkedList {
    fn new() -> Self {
        LinkedList { head: None }
    }
    
    fn append(&mut self, data: i32) {
        let new_node = Box::new(Node { data, next: None });
        
        match &mut self.head {
            None => self.head = Some(new_node),
            Some(head) => {
                let mut current = head;
                while current.next.is_some() {
                    current = current.next.as_mut().unwrap();
                }
                current.next = Some(new_node);
            }
        }
    }
    
    fn prepend(&mut self, data: i32) {
        let new_node = Box::new(Node {
            data,
            next: self.head.take(),
        });
        self.head = Some(new_node);
    }
    
    fn display(&self) {
        let mut current = &self.head;
        while let Some(node) = current {
            print!("{} -> ", node.data);
            current = &node.next;
        }
        println!("null");
    }
    
    fn search(&self, data: i32) -> bool {
        let mut current = &self.head;
        while let Some(node) = current {
            if node.data == data {
                return true;
            }
            current = &node.next;
        }
        false
    }
}

fn main() {
    let mut list = LinkedList::new();
    list.append(1);
    list.append(2);
    list.prepend(0);
    list.display();
    println!("Search 2: {}", list.search(2));
}""")

    # TypeScript
    with open(f"{base_dir}/linked_list.ts", "w") as f:
        f.write("""class ListNode {
    data: number;
    next: ListNode | null = null;
    
    constructor(data: number) {
        this.data = data;
    }
}

class LinkedList {
    private head: ListNode | null = null;
    
    append(data: number): void {
        const newNode = new ListNode(data);
        
        if (!this.head) {
            this.head = newNode;
            return;
        }
        
        let current = this.head;
        while (current.next) {
            current = current.next;
        }
        current.next = newNode;
    }
    
    prepend(data: number): void {
        const newNode = new ListNode(data);
        newNode.next = this.head;
        this.head = newNode;
    }
    
    display(): void {
        let current = this.head;
        const values: string[] = [];
        while (current) {
            values.push(current.data.toString());
            current = current.next;
        }
        console.log(values.join(" -> ") + " -> null");
    }
    
    search(data: number): boolean {
        let current = this.head;
        while (current) {
            if (current.data === data) return true;
            current = current.next;
        }
        return false;
    }
}

const list = new LinkedList();
list.append(1);
list.append(2);
list.prepend(0);
list.display();
console.log("Search 2:", list.search(2));""")

def complete_heap_sort():
    """Completa Heap Sort implementações pequenas"""
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/heap-sort"
    
    # Kotlin
    with open(f"{base_dir}/HeapSort.kt", "w") as f:
        f.write("""fun heapify(arr: IntArray, n: Int, i: Int) {
    var largest = i
    val left = 2 * i + 1
    val right = 2 * i + 2
    
    if (left < n && arr[left] > arr[largest]) largest = left
    if (right < n && arr[right] > arr[largest]) largest = right
    
    if (largest != i) {
        val temp = arr[i]
        arr[i] = arr[largest]
        arr[largest] = temp
        heapify(arr, n, largest)
    }
}

fun heapSort(arr: IntArray) {
    val n = arr.size
    
    for (i in n / 2 - 1 downTo 0) {
        heapify(arr, n, i)
    }
    
    for (i in n - 1 downTo 1) {
        val temp = arr[0]
        arr[0] = arr[i]
        arr[i] = temp
        heapify(arr, i, 0)
    }
}

fun main() {
    val arr = intArrayOf(64, 34, 25, 12, 22, 11, 90)
    heapSort(arr)
    println(arr.contentToString())
}""")

    # Rust
    with open(f"{base_dir}/heap_sort.rs", "w") as f:
        f.write("""fn heapify(arr: &mut [i32], n: usize, i: usize) {
    let mut largest = i;
    let left = 2 * i + 1;
    let right = 2 * i + 2;
    
    if left < n && arr[left] > arr[largest] {
        largest = left;
    }
    
    if right < n && arr[right] > arr[largest] {
        largest = right;
    }
    
    if largest != i {
        arr.swap(i, largest);
        heapify(arr, n, largest);
    }
}

fn heap_sort(arr: &mut [i32]) {
    let n = arr.len();
    
    for i in (0..n/2).rev() {
        heapify(arr, n, i);
    }
    
    for i in (1..n).rev() {
        arr.swap(0, i);
        heapify(arr, i, 0);
    }
}

fn main() {
    let mut arr = [64, 34, 25, 12, 22, 11, 90];
    heap_sort(&mut arr);
    println!("{:?}", arr);
}""")

    # TypeScript
    with open(f"{base_dir}/heap_sort.ts", "w") as f:
        f.write("""function heapify(arr: number[], n: number, i: number): void {
    let largest = i;
    const left = 2 * i + 1;
    const right = 2 * i + 2;
    
    if (left < n && arr[left] > arr[largest]) largest = left;
    if (right < n && arr[right] > arr[largest]) largest = right;
    
    if (largest !== i) {
        [arr[i], arr[largest]] = [arr[largest], arr[i]];
        heapify(arr, n, largest);
    }
}

function heapSort(arr: number[]): void {
    const n = arr.length;
    
    for (let i = Math.floor(n / 2) - 1; i >= 0; i--) {
        heapify(arr, n, i);
    }
    
    for (let i = n - 1; i > 0; i--) {
        [arr[0], arr[i]] = [arr[i], arr[0]];
        heapify(arr, i, 0);
    }
}

const arr = [64, 34, 25, 12, 22, 11, 90];
heapSort(arr);
console.log(arr);""")

if __name__ == "__main__":
    print("Completando segunda fase...")
    complete_dynamic_programming()
    complete_linked_list()
    complete_heap_sort()
    print("Segunda fase completada!")
