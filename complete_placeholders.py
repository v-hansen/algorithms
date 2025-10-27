#!/usr/bin/env python3
import os

def complete_quick_sort():
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/quick-sort"
    
    # Clojure
    with open(f"{base_dir}/quick_sort.clj", "w") as f:
        f.write("""(defn quick-sort [arr]
  (if (<= (count arr) 1)
    arr
    (let [pivot (first arr)
          rest-arr (rest arr)
          less (filter #(< % pivot) rest-arr)
          greater (filter #(>= % pivot) rest-arr)]
      (concat (quick-sort less) [pivot] (quick-sort greater)))))

(println (quick-sort [64 34 25 12 22 11 90]))""")

    # Ruby
    with open(f"{base_dir}/quick_sort.rb", "w") as f:
        f.write("""def quick_sort(arr)
  return arr if arr.length <= 1
  pivot = arr[0]
  less = arr[1..-1].select { |x| x < pivot }
  greater = arr[1..-1].select { |x| x >= pivot }
  quick_sort(less) + [pivot] + quick_sort(greater)
end

puts quick_sort([64,34,25,12,22,11,90]).inspect""")

def complete_bfs():
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/breadth-first-search"
    
    # Ruby
    with open(f"{base_dir}/breadth_first_search.rb", "w") as f:
        f.write("""def bfs(graph, start)
  visited = Set.new
  queue = [start]
  visited.add(start)
  
  while !queue.empty?
    node = queue.shift
    print "#{node} "
    (graph[node] || []).each do |neighbor|
      unless visited.include?(neighbor)
        visited.add(neighbor)
        queue.push(neighbor)
      end
    end
  end
end

graph = {0 => [1, 2], 1 => [2], 2 => [0, 3], 3 => [3]}
bfs(graph, 2)""")

    # Clojure
    with open(f"{base_dir}/breadth_first_search.clj", "w") as f:
        f.write("""(defn bfs [graph start]
  (loop [queue [start] visited #{start}]
    (when (seq queue)
      (let [node (first queue)
            neighbors (get graph node [])
            new-neighbors (remove visited neighbors)
            new-visited (into visited new-neighbors)
            new-queue (into (vec (rest queue)) new-neighbors)]
        (print node " ")
        (recur new-queue new-visited)))))

(def graph {0 [1 2] 1 [2] 2 [0 3] 3 [3]})
(bfs graph 2)""")

def complete_dijkstra():
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/dijkstra-algorithm"
    
    # Python
    with open(f"{base_dir}/dijkstra_algorithm.py", "w") as f:
        f.write("""import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_distance, current = heapq.heappop(pq)
        if current_distance > distances[current]:
            continue
        for neighbor, weight in graph[current].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

graph = {'A': {'B': 1, 'C': 4}, 'B': {'C': 2, 'D': 5}, 'C': {'D': 1}, 'D': {}}
print(dijkstra(graph, 'A'))""")

    # JavaScript
    with open(f"{base_dir}/dijkstra_algorithm.js", "w") as f:
        f.write("""function dijkstra(graph, start) {
    const distances = {};
    const pq = [[0, start]];
    
    for (let node in graph) distances[node] = Infinity;
    distances[start] = 0;
    
    while (pq.length) {
        pq.sort((a, b) => a[0] - b[0]);
        const [currentDistance, current] = pq.shift();
        
        if (currentDistance > distances[current]) continue;
        
        for (let neighbor in graph[current]) {
            const distance = currentDistance + graph[current][neighbor];
            if (distance < distances[neighbor]) {
                distances[neighbor] = distance;
                pq.push([distance, neighbor]);
            }
        }
    }
    return distances;
}

const graph = {A: {B: 1, C: 4}, B: {C: 2, D: 5}, C: {D: 1}, D: {}};
console.log(dijkstra(graph, 'A'));""")

    # Ruby
    with open(f"{base_dir}/dijkstra_algorithm.rb", "w") as f:
        f.write("""def dijkstra(graph, start)
  distances = Hash.new(Float::INFINITY)
  distances[start] = 0
  pq = [[0, start]]
  
  while !pq.empty?
    pq.sort!
    current_distance, current = pq.shift
    next if current_distance > distances[current]
    
    graph[current].each do |neighbor, weight|
      distance = current_distance + weight
      if distance < distances[neighbor]
        distances[neighbor] = distance
        pq.push([distance, neighbor])
      end
    end
  end
  distances
end

graph = {'A' => {'B' => 1, 'C' => 4}, 'B' => {'C' => 2, 'D' => 5}, 'C' => {'D' => 1}, 'D' => {}}
puts dijkstra(graph, 'A').inspect""")

    # Clojure
    with open(f"{base_dir}/dijkstra_algorithm.clj", "w") as f:
        f.write("""(defn dijkstra [graph start]
  (loop [distances (assoc (zipmap (keys graph) (repeat Double/POSITIVE_INFINITY)) start 0)
         pq [[0 start]]]
    (if (empty? pq)
      distances
      (let [[current-distance current] (first (sort pq))
            remaining-pq (remove #(= % [current-distance current]) pq)]
        (if (> current-distance (get distances current))
          (recur distances remaining-pq)
          (let [neighbors (get graph current {})
                updates (for [[neighbor weight] neighbors
                             :let [distance (+ current-distance weight)]
                             :when (< distance (get distances neighbor))]
                         [neighbor distance])
                new-distances (reduce (fn [d [n dist]] (assoc d n dist)) distances updates)
                new-pq (concat remaining-pq (map (fn [[n d]] [d n]) updates))]
            (recur new-distances new-pq)))))))

(def graph {"A" {"B" 1 "C" 4} "B" {"C" 2 "D" 5} "C" {"D" 1} "D" {}})
(println (dijkstra graph "A"))""")

def complete_hash_table():
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/hash-table"
    
    # Ruby
    with open(f"{base_dir}/hash_table.rb", "w") as f:
        f.write("""class HashTable
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
puts ht.get("key1")""")

    # Clojure
    with open(f"{base_dir}/hash_table.clj", "w") as f:
        f.write("""(defn make-hash-table [size]
  {:size size :buckets (vec (repeat size []))})

(defn hash-fn [key size]
  (mod (hash key) size))

(defn put [ht key value]
  (let [index (hash-fn key (:size ht))
        bucket (nth (:buckets ht) index)
        new-bucket (conj (remove #(= (first %) key) bucket) [key value])]
    (assoc-in ht [:buckets index] new-bucket)))

(defn get-val [ht key]
  (let [index (hash-fn key (:size ht))
        bucket (nth (:buckets ht) index)
        pair (first (filter #(= (first %) key) bucket))]
    (when pair (second pair))))

(def ht (-> (make-hash-table 10)
            (put "key1" "value1")))
(println (get-val ht "key1"))""")

if __name__ == "__main__":
    print("Completando placeholders críticos...")
    complete_quick_sort()
    complete_bfs()
    complete_dijkstra()
    complete_hash_table()
    print("Placeholders críticos completados!")
