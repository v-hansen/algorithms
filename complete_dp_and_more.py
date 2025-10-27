#!/usr/bin/env python3
import os

def complete_dynamic_programming():
    """Completa todos os algoritmos de programação dinâmica"""
    
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/dynamic-programming"
    
    dp_implementations = {
        "dynamic_programming.c": """#include <stdio.h>
#include <stdlib.h>

int fibonacci(int n) {
    if (n <= 1) return n;
    int dp[n+1];
    dp[0] = 0; dp[1] = 1;
    for (int i = 2; i <= n; i++) {
        dp[i] = dp[i-1] + dp[i-2];
    }
    return dp[n];
}

int coinChange(int coins[], int m, int amount) {
    int dp[amount + 1];
    dp[0] = 0;
    for (int i = 1; i <= amount; i++) dp[i] = amount + 1;
    
    for (int i = 1; i <= amount; i++) {
        for (int j = 0; j < m; j++) {
            if (coins[j] <= i) {
                dp[i] = dp[i] < dp[i - coins[j]] + 1 ? dp[i] : dp[i - coins[j]] + 1;
            }
        }
    }
    return dp[amount] > amount ? -1 : dp[amount];
}

int main() {
    printf("Fibonacci(10): %d\\n", fibonacci(10));
    int coins[] = {1, 3, 4};
    printf("Coin change: %d\\n", coinChange(coins, 3, 6));
    return 0;
}""",
        
        "dynamic_programming.cpp": """#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int fibonacci(int n) {
    if (n <= 1) return n;
    vector<int> dp(n + 1);
    dp[0] = 0; dp[1] = 1;
    for (int i = 2; i <= n; i++) {
        dp[i] = dp[i-1] + dp[i-2];
    }
    return dp[n];
}

int coinChange(vector<int>& coins, int amount) {
    vector<int> dp(amount + 1, amount + 1);
    dp[0] = 0;
    
    for (int i = 1; i <= amount; i++) {
        for (int coin : coins) {
            if (coin <= i) {
                dp[i] = min(dp[i], dp[i - coin] + 1);
            }
        }
    }
    return dp[amount] > amount ? -1 : dp[amount];
}

int knapsack(vector<int>& weights, vector<int>& values, int capacity) {
    int n = weights.size();
    vector<vector<int>> dp(n + 1, vector<int>(capacity + 1, 0));
    
    for (int i = 1; i <= n; i++) {
        for (int w = 1; w <= capacity; w++) {
            if (weights[i-1] <= w) {
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1]);
            } else {
                dp[i][w] = dp[i-1][w];
            }
        }
    }
    return dp[n][capacity];
}

int main() {
    cout << "Fibonacci(10): " << fibonacci(10) << endl;
    
    vector<int> coins = {1, 3, 4};
    cout << "Coin change: " << coinChange(coins, 6) << endl;
    
    vector<int> weights = {2, 1, 3};
    vector<int> values = {4, 2, 3};
    cout << "Knapsack: " << knapsack(weights, values, 4) << endl;
    
    return 0;
}""",
        
        "dynamic_programming.go": """package main
import "fmt"

func fibonacci(n int) int {
    if n <= 1 {
        return n
    }
    dp := make([]int, n+1)
    dp[0], dp[1] = 0, 1
    for i := 2; i <= n; i++ {
        dp[i] = dp[i-1] + dp[i-2]
    }
    return dp[n]
}

func coinChange(coins []int, amount int) int {
    dp := make([]int, amount+1)
    for i := 1; i <= amount; i++ {
        dp[i] = amount + 1
    }
    
    for i := 1; i <= amount; i++ {
        for _, coin := range coins {
            if coin <= i {
                if dp[i-coin]+1 < dp[i] {
                    dp[i] = dp[i-coin] + 1
                }
            }
        }
    }
    
    if dp[amount] > amount {
        return -1
    }
    return dp[amount]
}

func knapsack(weights, values []int, capacity int) int {
    n := len(weights)
    dp := make([][]int, n+1)
    for i := range dp {
        dp[i] = make([]int, capacity+1)
    }
    
    for i := 1; i <= n; i++ {
        for w := 1; w <= capacity; w++ {
            if weights[i-1] <= w {
                include := dp[i-1][w-weights[i-1]] + values[i-1]
                exclude := dp[i-1][w]
                if include > exclude {
                    dp[i][w] = include
                } else {
                    dp[i][w] = exclude
                }
            } else {
                dp[i][w] = dp[i-1][w]
            }
        }
    }
    return dp[n][capacity]
}

func main() {
    fmt.Printf("Fibonacci(10): %d\\n", fibonacci(10))
    fmt.Printf("Coin change: %d\\n", coinChange([]int{1, 3, 4}, 6))
    fmt.Printf("Knapsack: %d\\n", knapsack([]int{2, 1, 3}, []int{4, 2, 3}, 4))
}""",
        
        "dynamic_programming.php": """<?php
function fibonacci($n) {
    if ($n <= 1) return $n;
    $dp = array_fill(0, $n + 1, 0);
    $dp[1] = 1;
    
    for ($i = 2; $i <= $n; $i++) {
        $dp[$i] = $dp[$i-1] + $dp[$i-2];
    }
    return $dp[$n];
}

function coinChange($coins, $amount) {
    $dp = array_fill(0, $amount + 1, $amount + 1);
    $dp[0] = 0;
    
    for ($i = 1; $i <= $amount; $i++) {
        foreach ($coins as $coin) {
            if ($coin <= $i) {
                $dp[$i] = min($dp[$i], $dp[$i - $coin] + 1);
            }
        }
    }
    
    return $dp[$amount] > $amount ? -1 : $dp[$amount];
}

function knapsack($weights, $values, $capacity) {
    $n = count($weights);
    $dp = array_fill(0, $n + 1, array_fill(0, $capacity + 1, 0));
    
    for ($i = 1; $i <= $n; $i++) {
        for ($w = 1; $w <= $capacity; $w++) {
            if ($weights[$i-1] <= $w) {
                $dp[$i][$w] = max(
                    $dp[$i-1][$w],
                    $dp[$i-1][$w-$weights[$i-1]] + $values[$i-1]
                );
            } else {
                $dp[$i][$w] = $dp[$i-1][$w];
            }
        }
    }
    return $dp[$n][$capacity];
}

echo "Fibonacci(10): " . fibonacci(10) . "\\n";
echo "Coin change: " . coinChange([1, 3, 4], 6) . "\\n";
echo "Knapsack: " . knapsack([2, 1, 3], [4, 2, 3], 4) . "\\n";
?>""",
        
        "dynamic_programming.cs": """using System;
using System.Linq;

class DynamicProgramming {
    static int Fibonacci(int n) {
        if (n <= 1) return n;
        int[] dp = new int[n + 1];
        dp[0] = 0; dp[1] = 1;
        
        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];
    }
    
    static int CoinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Array.Fill(dp, amount + 1);
        dp[0] = 0;
        
        for (int i = 1; i <= amount; i++) {
            foreach (int coin in coins) {
                if (coin <= i) {
                    dp[i] = Math.Min(dp[i], dp[i - coin] + 1);
                }
            }
        }
        
        return dp[amount] > amount ? -1 : dp[amount];
    }
    
    static int Knapsack(int[] weights, int[] values, int capacity) {
        int n = weights.Length;
        int[,] dp = new int[n + 1, capacity + 1];
        
        for (int i = 1; i <= n; i++) {
            for (int w = 1; w <= capacity; w++) {
                if (weights[i-1] <= w) {
                    dp[i,w] = Math.Max(dp[i-1,w], dp[i-1,w-weights[i-1]] + values[i-1]);
                } else {
                    dp[i,w] = dp[i-1,w];
                }
            }
        }
        return dp[n,capacity];
    }
    
    static void Main() {
        Console.WriteLine($"Fibonacci(10): {Fibonacci(10)}");
        Console.WriteLine($"Coin change: {CoinChange(new int[]{1, 3, 4}, 6)}");
        Console.WriteLine($"Knapsack: {Knapsack(new int[]{2, 1, 3}, new int[]{4, 2, 3}, 4)}");
    }
}"""
    }
    
    for filename, code in dp_implementations.items():
        with open(f"{base_dir}/{filename}", "w") as f:
            f.write(code)

def complete_linked_list():
    """Completa implementações de linked list"""
    
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/linked-list"
    
    ll_implementations = {
        "linked_list.c": """#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

typedef struct {
    Node* head;
} LinkedList;

LinkedList* createList() {
    LinkedList* list = malloc(sizeof(LinkedList));
    list->head = NULL;
    return list;
}

void append(LinkedList* list, int data) {
    Node* newNode = malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    
    if (!list->head) {
        list->head = newNode;
        return;
    }
    
    Node* current = list->head;
    while (current->next) current = current->next;
    current->next = newNode;
}

void display(LinkedList* list) {
    Node* current = list->head;
    while (current) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\\n");
}

int main() {
    LinkedList* list = createList();
    append(list, 1);
    append(list, 2);
    append(list, 3);
    display(list);
    return 0;
}""",
        
        "linked_list.cpp": """#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;
    
    Node(int data) : data(data), next(nullptr) {}
};

class LinkedList {
private:
    Node* head;
    
public:
    LinkedList() : head(nullptr) {}
    
    void append(int data) {
        Node* newNode = new Node(data);
        
        if (!head) {
            head = newNode;
            return;
        }
        
        Node* current = head;
        while (current->next) current = current->next;
        current->next = newNode;
    }
    
    void prepend(int data) {
        Node* newNode = new Node(data);
        newNode->next = head;
        head = newNode;
    }
    
    void display() {
        Node* current = head;
        while (current) {
            cout << current->data << " -> ";
            current = current->next;
        }
        cout << "NULL" << endl;
    }
    
    bool search(int data) {
        Node* current = head;
        while (current) {
            if (current->data == data) return true;
            current = current->next;
        }
        return false;
    }
};

int main() {
    LinkedList list;
    list.append(1);
    list.append(2);
    list.prepend(0);
    list.display();
    cout << "Search 2: " << (list.search(2) ? "Found" : "Not found") << endl;
    return 0;
}""",
        
        "linked_list.go": """package main
import "fmt"

type Node struct {
    data int
    next *Node
}

type LinkedList struct {
    head *Node
}

func (ll *LinkedList) Append(data int) {
    newNode := &Node{data: data}
    
    if ll.head == nil {
        ll.head = newNode
        return
    }
    
    current := ll.head
    for current.next != nil {
        current = current.next
    }
    current.next = newNode
}

func (ll *LinkedList) Prepend(data int) {
    newNode := &Node{data: data, next: ll.head}
    ll.head = newNode
}

func (ll *LinkedList) Display() {
    current := ll.head
    for current != nil {
        fmt.Print(current.data, " -> ")
        current = current.next
    }
    fmt.Println("nil")
}

func (ll *LinkedList) Search(data int) bool {
    current := ll.head
    for current != nil {
        if current.data == data {
            return true
        }
        current = current.next
    }
    return false
}

func main() {
    ll := &LinkedList{}
    ll.Append(1)
    ll.Append(2)
    ll.Prepend(0)
    ll.Display()
    fmt.Printf("Search 2: %t\\n", ll.Search(2))
}""",
        
        "linked_list.php": """<?php
class Node {
    public $data;
    public $next;
    
    public function __construct($data) {
        $this->data = $data;
        $this->next = null;
    }
}

class LinkedList {
    private $head;
    
    public function __construct() {
        $this->head = null;
    }
    
    public function append($data) {
        $newNode = new Node($data);
        
        if ($this->head === null) {
            $this->head = $newNode;
            return;
        }
        
        $current = $this->head;
        while ($current->next !== null) {
            $current = $current->next;
        }
        $current->next = $newNode;
    }
    
    public function prepend($data) {
        $newNode = new Node($data);
        $newNode->next = $this->head;
        $this->head = $newNode;
    }
    
    public function display() {
        $current = $this->head;
        while ($current !== null) {
            echo $current->data . " -> ";
            $current = $current->next;
        }
        echo "NULL\\n";
    }
    
    public function search($data) {
        $current = $this->head;
        while ($current !== null) {
            if ($current->data === $data) {
                return true;
            }
            $current = $current->next;
        }
        return false;
    }
}

$list = new LinkedList();
$list->append(1);
$list->append(2);
$list->prepend(0);
$list->display();
echo "Search 2: " . ($list->search(2) ? "Found" : "Not found") . "\\n";
?>""",
        
        "linked_list.cs": """using System;

class Node {
    public int data;
    public Node next;
    
    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    private Node head;
    
    public void Append(int data) {
        Node newNode = new Node(data);
        
        if (head == null) {
            head = newNode;
            return;
        }
        
        Node current = head;
        while (current.next != null) {
            current = current.next;
        }
        current.next = newNode;
    }
    
    public void Prepend(int data) {
        Node newNode = new Node(data);
        newNode.next = head;
        head = newNode;
    }
    
    public void Display() {
        Node current = head;
        while (current != null) {
            Console.Write(current.data + " -> ");
            current = current.next;
        }
        Console.WriteLine("NULL");
    }
    
    public bool Search(int data) {
        Node current = head;
        while (current != null) {
            if (current.data == data) return true;
            current = current.next;
        }
        return false;
    }
}

class Program {
    static void Main() {
        LinkedList list = new LinkedList();
        list.Append(1);
        list.Append(2);
        list.Prepend(0);
        list.Display();
        Console.WriteLine("Search 2: " + (list.Search(2) ? "Found" : "Not found"));
    }
}"""
    }
    
    for filename, code in ll_implementations.items():
        with open(f"{base_dir}/{filename}", "w") as f:
            f.write(code)

if __name__ == "__main__":
    print("Completando programação dinâmica e estruturas de dados...")
    complete_dynamic_programming()
    complete_linked_list()
    print("Programação dinâmica e estruturas de dados completadas!")
