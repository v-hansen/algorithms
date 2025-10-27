#!/usr/bin/env python3
import os

def create_binary_search_implementations():
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/binary-search"
    
    # Ruby
    with open(f"{base_dir}/binary-search.rb", "w") as f:
        f.write("""def binary_search(arr, target)
  left, right = 0, arr.length - 1
  while left <= right
    mid = (left + right) / 2
    return mid if arr[mid] == target
    arr[mid] < target ? left = mid + 1 : right = mid - 1
  end
  -1
end

puts binary_search([1,2,3,4,5], 3)""")

    # Clojure
    with open(f"{base_dir}/binary-search.clj", "w") as f:
        f.write("""(defn binary-search [arr target]
  (loop [left 0 right (dec (count arr))]
    (when (<= left right)
      (let [mid (quot (+ left right) 2)]
        (cond
          (= (nth arr mid) target) mid
          (< (nth arr mid) target) (recur (inc mid) right)
          :else (recur left (dec mid)))))))

(println (binary-search [1 2 3 4 5] 3))""")

def create_linear_search_implementations():
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/linear-search"
    
    # Todas as implementações pequenas precisam ser expandidas
    implementations = {
        "linear-search.py": """def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

print(linear_search([1,2,3,4,5], 3))""",
        
        "linear-search.js": """function linearSearch(arr, target) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === target) return i;
    }
    return -1;
}

console.log(linearSearch([1,2,3,4,5], 3));""",
        
        "linear-search.rb": """def linear_search(arr, target)
  arr.each_with_index { |val, i| return i if val == target }
  -1
end

puts linear_search([1,2,3,4,5], 3)""",
        
        "linear-search.clj": """(defn linear-search [arr target]
  (loop [i 0]
    (cond
      (>= i (count arr)) -1
      (= (nth arr i) target) i
      :else (recur (inc i)))))

(println (linear-search [1 2 3 4 5] 3))"""
    }
    
    for filename, code in implementations.items():
        with open(f"{base_dir}/{filename}", "w") as f:
            f.write(code)

def create_heap_sort_placeholders():
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/heap-sort"
    
    # JavaScript
    with open(f"{base_dir}/heap_sort.js", "w") as f:
        f.write("""function heapSort(arr) {
    function heapify(arr, n, i) {
        let largest = i, left = 2*i+1, right = 2*i+2;
        if (left < n && arr[left] > arr[largest]) largest = left;
        if (right < n && arr[right] > arr[largest]) largest = right;
        if (largest !== i) {
            [arr[i], arr[largest]] = [arr[largest], arr[i]];
            heapify(arr, n, largest);
        }
    }
    
    for (let i = Math.floor(arr.length/2)-1; i >= 0; i--) heapify(arr, arr.length, i);
    for (let i = arr.length-1; i > 0; i--) {
        [arr[0], arr[i]] = [arr[i], arr[0]];
        heapify(arr, i, 0);
    }
    return arr;
}

console.log(heapSort([64,34,25,12,22,11,90]));""")

    # Ruby
    with open(f"{base_dir}/heap_sort.rb", "w") as f:
        f.write("""def heap_sort(arr)
  def heapify(arr, n, i)
    largest = i
    left, right = 2*i+1, 2*i+2
    largest = left if left < n && arr[left] > arr[largest]
    largest = right if right < n && arr[right] > arr[largest]
    if largest != i
      arr[i], arr[largest] = arr[largest], arr[i]
      heapify(arr, n, largest)
    end
  end
  
  (arr.length/2-1).downto(0) { |i| heapify(arr, arr.length, i) }
  (arr.length-1).downto(1) do |i|
    arr[0], arr[i] = arr[i], arr[0]
    heapify(arr, i, 0)
  end
  arr
end

puts heap_sort([64,34,25,12,22,11,90]).inspect""")

    # Clojure
    with open(f"{base_dir}/heap_sort.clj", "w") as f:
        f.write("""(defn heapify [arr n i]
  (let [left (+ (* 2 i) 1)
        right (+ (* 2 i) 2)
        largest (cond
                  (and (< left n) (> (nth arr left) (nth arr i))) left
                  :else i)
        largest (cond
                  (and (< right n) (> (nth arr right) (nth arr largest))) right
                  :else largest)]
    (if (not= largest i)
      (let [new-arr (assoc arr i (nth arr largest) largest (nth arr i))]
        (heapify new-arr n largest))
      arr)))

(defn heap-sort [arr]
  (let [n (count arr)
        arr (reduce #(heapify %1 n %2) arr (range (dec (quot n 2)) -1 -1))]
    (reduce (fn [acc i]
              (let [new-arr (assoc acc 0 (nth acc i) i (nth acc 0))]
                (heapify new-arr i 0)))
            arr (range (dec n) 0 -1))))

(println (heap-sort [64 34 25 12 22 11 90]))""")

def create_dfs_implementations():
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/depth-first-search"
    
    # Python
    with open(f"{base_dir}/depth_first_search.py", "w") as f:
        f.write("""def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
dfs(graph, 2)""")

    # JavaScript
    with open(f"{base_dir}/depth_first_search.js", "w") as f:
        f.write("""function dfs(graph, start, visited = new Set()) {
    visited.add(start);
    process.stdout.write(start + ' ');
    (graph[start] || []).forEach(neighbor => {
        if (!visited.has(neighbor)) dfs(graph, neighbor, visited);
    });
    return visited;
}

const graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]};
dfs(graph, 2);""")

    # Ruby
    with open(f"{base_dir}/depth_first_search.rb", "w") as f:
        f.write("""def dfs(graph, start, visited = Set.new)
  visited.add(start)
  print "#{start} "
  (graph[start] || []).each do |neighbor|
    dfs(graph, neighbor, visited) unless visited.include?(neighbor)
  end
  visited
end

graph = {0 => [1, 2], 1 => [2], 2 => [0, 3], 3 => [3]}
dfs(graph, 2)""")

    # Clojure
    with open(f"{base_dir}/depth_first_search.clj", "w") as f:
        f.write("""(defn dfs [graph start visited]
  (let [new-visited (conj visited start)]
    (print start " ")
    (reduce (fn [v neighbor]
              (if (contains? v neighbor)
                v
                (dfs graph neighbor v)))
            new-visited
            (get graph start []))))

(def graph {0 [1 2] 1 [2] 2 [0 3] 3 [3]})
(dfs graph 2 #{})""")

if __name__ == "__main__":
    print("Completando implementações...")
    create_binary_search_implementations()
    create_linear_search_implementations()
    create_heap_sort_placeholders()
    create_dfs_implementations()
    print("Implementações básicas criadas!")
