# 📊 Algorithm Flowcharts & Diagrams

Visual representations of complex algorithms using Mermaid diagrams.

---

## Quick Sort

```mermaid
graph TD
    A[Start: Array] --> B{Array size <= 1?}
    B -->|Yes| C[Return array]
    B -->|No| D[Choose pivot]
    D --> E[Partition array]
    E --> F[Elements < pivot]
    E --> G[Pivot]
    E --> H[Elements > pivot]
    F --> I[Recursively sort left]
    H --> J[Recursively sort right]
    I --> K[Combine: left + pivot + right]
    J --> K
    K --> L[Return sorted array]
```

---

## Dijkstra's Algorithm

```mermaid
graph TD
    A[Start: Graph + Source] --> B[Initialize distances to ∞]
    B --> C[Set source distance to 0]
    C --> D[Create priority queue]
    D --> E{Queue empty?}
    E -->|Yes| F[Return distances]
    E -->|No| G[Extract min distance node]
    G --> H{For each neighbor}
    H --> I[Calculate new distance]
    I --> J{New distance < current?}
    J -->|Yes| K[Update distance]
    J -->|No| H
    K --> L[Add to queue]
    L --> H
    H --> E
```

---

## Merge Sort

```mermaid
graph TD
    A[Start: Array] --> B{Array size <= 1?}
    B -->|Yes| C[Return array]
    B -->|No| D[Find middle point]
    D --> E[Split into left half]
    D --> F[Split into right half]
    E --> G[Recursively sort left]
    F --> H[Recursively sort right]
    G --> I[Merge sorted halves]
    H --> I
    I --> J[Return merged array]
```

---

## Binary Search Tree Insert

```mermaid
graph TD
    A[Start: Insert value] --> B{Tree empty?}
    B -->|Yes| C[Create root node]
    B -->|No| D[Start at root]
    D --> E{Value < current?}
    E -->|Yes| F{Left child exists?}
    E -->|No| G{Right child exists?}
    F -->|Yes| H[Move to left child]
    F -->|No| I[Insert as left child]
    G -->|Yes| J[Move to right child]
    G -->|No| K[Insert as right child]
    H --> E
    J --> E
    I --> L[End]
    K --> L
    C --> L
```

---

## Dynamic Programming Pattern

```mermaid
graph TD
    A[Problem] --> B{Overlapping subproblems?}
    B -->|No| C[Use divide & conquer]
    B -->|Yes| D{Optimal substructure?}
    D -->|No| E[Not suitable for DP]
    D -->|Yes| F[Choose DP approach]
    F --> G[Top-down: Memoization]
    F --> H[Bottom-up: Tabulation]
    G --> I[Recursive + cache]
    H --> J[Iterative + table]
    I --> K[Solve problem]
    J --> K
```

---

## Breadth-First Search (BFS)

```mermaid
graph TD
    A[Start: Graph + Source] --> B[Create queue]
    B --> C[Mark source as visited]
    C --> D[Enqueue source]
    D --> E{Queue empty?}
    E -->|Yes| F[End]
    E -->|No| G[Dequeue node]
    G --> H[Process node]
    H --> I{For each neighbor}
    I --> J{Visited?}
    J -->|Yes| I
    J -->|No| K[Mark as visited]
    K --> L[Enqueue neighbor]
    L --> I
    I --> E
```

---

## Depth-First Search (DFS)

```mermaid
graph TD
    A[Start: Graph + Source] --> B[Create stack]
    B --> C[Push source]
    C --> D{Stack empty?}
    D -->|Yes| E[End]
    D -->|No| F[Pop node]
    F --> G{Visited?}
    G -->|Yes| D
    G -->|No| H[Mark as visited]
    H --> I[Process node]
    I --> J{For each neighbor}
    J --> K[Push neighbor]
    K --> J
    J --> D
```

---

## Hash Table Operations

```mermaid
graph TD
    A[Operation: Insert/Search/Delete] --> B[Compute hash of key]
    B --> C[Calculate index: hash % size]
    C --> D{Collision?}
    D -->|No| E[Direct access]
    D -->|Yes| F{Collision resolution}
    F --> G[Chaining: Linked list]
    F --> H[Open addressing: Probe]
    G --> I[Traverse chain]
    H --> J[Find next slot]
    I --> K[Perform operation]
    J --> K
    E --> K
```

---

## KMP Pattern Matching

```mermaid
graph TD
    A[Start: Text + Pattern] --> B[Build LPS array]
    B --> C[Initialize i=0, j=0]
    C --> D{i < text length?}
    D -->|No| E[Pattern not found]
    D -->|Yes| F{text[i] == pattern[j]?}
    F -->|Yes| G[i++, j++]
    F -->|No| H{j != 0?}
    H -->|Yes| I[j = LPS[j-1]]
    H -->|No| J[i++]
    G --> K{j == pattern length?}
    K -->|Yes| L[Pattern found at i-j]
    K -->|No| D
    I --> D
    J --> D
```

---

## Topological Sort (Kahn's Algorithm)

```mermaid
graph TD
    A[Start: DAG] --> B[Calculate in-degrees]
    B --> C[Find nodes with in-degree 0]
    C --> D[Add to queue]
    D --> E{Queue empty?}
    E -->|Yes| F{All nodes processed?}
    E -->|No| G[Dequeue node]
    G --> H[Add to result]
    H --> I{For each neighbor}
    I --> J[Decrease in-degree]
    J --> K{In-degree == 0?}
    K -->|Yes| L[Add to queue]
    K -->|No| I
    L --> I
    I --> E
    F -->|Yes| M[Return topological order]
    F -->|No| N[Cycle detected!]
```

---

## Decision Tree Training

```mermaid
graph TD
    A[Start: Training data] --> B{Pure node or max depth?}
    B -->|Yes| C[Create leaf node]
    B -->|No| D[Find best split]
    D --> E[Calculate information gain]
    E --> F[Split data]
    F --> G[Create left subtree]
    F --> H[Create right subtree]
    G --> I[Recursively build left]
    H --> J[Recursively build right]
    I --> K[Return tree]
    J --> K
    C --> K
```

---

## K-Means Clustering

```mermaid
graph TD
    A[Start: Data + K] --> B[Initialize K centroids]
    B --> C[Assign points to nearest centroid]
    C --> D[Calculate new centroids]
    D --> E{Centroids changed?}
    E -->|Yes| C
    E -->|No| F[Return clusters]
```

---

## Knapsack Dynamic Programming

```mermaid
graph TD
    A[Start: Items + Capacity] --> B[Create DP table]
    B --> C[Initialize first row/column to 0]
    C --> D{For each item i}
    D --> E{For each capacity w}
    E --> F{Item weight <= w?}
    F -->|No| G[DP[i][w] = DP[i-1][w]]
    F -->|Yes| H[Calculate with/without item]
    H --> I[DP[i][w] = max of both]
    I --> E
    G --> E
    E --> D
    D --> J[Return DP[n][W]]
```

---

## Algorithm Complexity Comparison

```mermaid
graph LR
    A[O1: Constant] --> B[O log n: Logarithmic]
    B --> C[On: Linear]
    C --> D[On log n: Linearithmic]
    D --> E[On²: Quadratic]
    E --> F[On³: Cubic]
    F --> G[O2ⁿ: Exponential]
    
    style A fill:#90EE90
    style B fill:#98FB98
    style C fill:#FFFFE0
    style D fill:#FFD700
    style E fill:#FFA500
    style F fill:#FF6347
    style G fill:#DC143C
```

---

## Data Structure Selection Guide

```mermaid
graph TD
    A[Need data structure] --> B{Need ordering?}
    B -->|No| C{Fast lookup?}
    B -->|Yes| D{Frequent insertions?}
    C -->|Yes| E[Hash Table]
    C -->|No| F[Array/List]
    D -->|Yes| G[Balanced BST]
    D -->|No| H[Sorted Array]
    
    I[Need prefix matching?] --> J[Trie]
    K[Need FIFO?] --> L[Queue]
    M[Need LIFO?] --> N[Stack]
    O[Need priority?] --> P[Heap]
```

---

**Note:** These diagrams are rendered automatically on GitHub and in Markdown viewers that support Mermaid syntax.

**Last Updated:** October 2025  
**Maintained by:** Vitor Hansen
