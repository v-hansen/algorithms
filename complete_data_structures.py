#!/usr/bin/env python3
import os

def complete_binary_search_tree():
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/binary-search-tree"
    
    # JavaScript
    with open(f"{base_dir}/binary_search_tree.js", "w") as f:
        f.write("""class Node {
    constructor(data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

class BST {
    constructor() { this.root = null; }
    
    insert(data) {
        this.root = this.insertNode(this.root, data);
    }
    
    insertNode(node, data) {
        if (!node) return new Node(data);
        if (data < node.data) node.left = this.insertNode(node.left, data);
        else node.right = this.insertNode(node.right, data);
        return node;
    }
    
    search(data) {
        return this.searchNode(this.root, data);
    }
    
    searchNode(node, data) {
        if (!node || node.data === data) return node;
        return data < node.data ? this.searchNode(node.left, data) : this.searchNode(node.right, data);
    }
}

const bst = new BST();
[50, 30, 70, 20, 40].forEach(x => bst.insert(x));
console.log(bst.search(40) ? "Found" : "Not found");""")

    # Ruby
    with open(f"{base_dir}/binary_search_tree.rb", "w") as f:
        f.write("""class Node
  attr_accessor :data, :left, :right
  def initialize(data)
    @data, @left, @right = data, nil, nil
  end
end

class BST
  def initialize
    @root = nil
  end
  
  def insert(data)
    @root = insert_node(@root, data)
  end
  
  def insert_node(node, data)
    return Node.new(data) unless node
    if data < node.data
      node.left = insert_node(node.left, data)
    else
      node.right = insert_node(node.right, data)
    end
    node
  end
  
  def search(data)
    search_node(@root, data)
  end
  
  def search_node(node, data)
    return node if !node || node.data == data
    data < node.data ? search_node(node.left, data) : search_node(node.right, data)
  end
end

bst = BST.new
[50, 30, 70, 20, 40].each { |x| bst.insert(x) }
puts bst.search(40) ? "Found" : "Not found" """)

    # Clojure
    with open(f"{base_dir}/binary_search_tree.clj", "w") as f:
        f.write("""(defn make-node [data] {:data data :left nil :right nil})

(defn insert-node [node data]
  (cond
    (nil? node) (make-node data)
    (< data (:data node)) (assoc node :left (insert-node (:left node) data))
    :else (assoc node :right (insert-node (:right node) data))))

(defn search-node [node data]
  (cond
    (or (nil? node) (= (:data node) data)) node
    (< data (:data node)) (search-node (:left node) data)
    :else (search-node (:right node) data)))

(def bst (reduce insert-node nil [50 30 70 20 40]))
(println (if (search-node bst 40) "Found" "Not found"))""")

def complete_linked_list():
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/linked-list"
    
    # Ruby
    with open(f"{base_dir}/linked_list.rb", "w") as f:
        f.write("""class Node
  attr_accessor :data, :next
  def initialize(data)
    @data, @next = data, nil
  end
end

class LinkedList
  def initialize
    @head = nil
  end
  
  def append(data)
    new_node = Node.new(data)
    if @head.nil?
      @head = new_node
    else
      current = @head
      current = current.next while current.next
      current.next = new_node
    end
  end
  
  def display
    current = @head
    while current
      print "#{current.data} -> "
      current = current.next
    end
    puts "nil"
  end
end

ll = LinkedList.new
[1, 2, 3].each { |x| ll.append(x) }
ll.display""")

    # Clojure
    with open(f"{base_dir}/linked_list.clj", "w") as f:
        f.write("""(defn make-node [data next] {:data data :next next})

(defn append [head data]
  (if (nil? head)
    (make-node data nil)
    (assoc head :next (append (:next head) data))))

(defn display [head]
  (when head
    (print (:data head) " -> ")
    (display (:next head))))

(def ll (reduce append nil [1 2 3]))
(display ll)
(println "nil")""")

def complete_dynamic_programming():
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/dynamic-programming"
    
    # JavaScript
    with open(f"{base_dir}/dynamic_programming.js", "w") as f:
        f.write("""// Fibonacci with memoization
function fibMemo(n, memo = {}) {
    if (n in memo) return memo[n];
    if (n <= 2) return 1;
    memo[n] = fibMemo(n - 1, memo) + fibMemo(n - 2, memo);
    return memo[n];
}

// Coin change problem
function coinChange(coins, amount) {
    const dp = new Array(amount + 1).fill(Infinity);
    dp[0] = 0;
    
    for (let coin of coins) {
        for (let i = coin; i <= amount; i++) {
            dp[i] = Math.min(dp[i], dp[i - coin] + 1);
        }
    }
    return dp[amount] === Infinity ? -1 : dp[amount];
}

console.log("Fib(10):", fibMemo(10));
console.log("Coin change:", coinChange([1, 3, 4], 6));""")

    # Ruby
    with open(f"{base_dir}/dynamic_programming.rb", "w") as f:
        f.write("""def fib_memo(n, memo = {})
  return memo[n] if memo.key?(n)
  return 1 if n <= 2
  memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
end

def coin_change(coins, amount)
  dp = Array.new(amount + 1, Float::INFINITY)
  dp[0] = 0
  
  coins.each do |coin|
    (coin..amount).each do |i|
      dp[i] = [dp[i], dp[i - coin] + 1].min
    end
  end
  dp[amount] == Float::INFINITY ? -1 : dp[amount]
end

puts "Fib(10): #{fib_memo(10)}"
puts "Coin change: #{coin_change([1, 3, 4], 6)}" """)

    # Clojure
    with open(f"{base_dir}/dynamic_programming.clj", "w") as f:
        f.write("""(def fib-memo
  (memoize (fn [n]
             (if (<= n 2) 1
                 (+ (fib-memo (- n 1)) (fib-memo (- n 2)))))))

(defn coin-change [coins amount]
  (let [dp (vec (concat [0] (repeat amount Double/POSITIVE_INFINITY)))]
    (loop [dp dp coin-idx 0]
      (if (>= coin-idx (count coins))
        (let [result (nth dp amount)]
          (if (= result Double/POSITIVE_INFINITY) -1 result))
        (let [coin (nth coins coin-idx)
              new-dp (reduce (fn [acc i]
                              (assoc acc i (min (nth acc i) (+ (nth acc (- i coin)) 1))))
                            dp (range coin (inc amount)))]
          (recur new-dp (inc coin-idx)))))))

(println "Fib(10):" (fib-memo 10))
(println "Coin change:" (coin-change [1 3 4] 6))""")

if __name__ == "__main__":
    print("Completando estruturas de dados...")
    complete_binary_search_tree()
    complete_linked_list()
    complete_dynamic_programming()
    print("Estruturas de dados completadas!")
