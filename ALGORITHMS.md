# 📚 Algorithm Reference Guide

Complete reference with complexity analysis, use cases, and implementation notes for all 34 algorithms.

---

## 🔍 Search Algorithms

### Binary Search
**Time Complexity:** O(log n)  
**Space Complexity:** O(1) iterative, O(log n) recursive  
**Best For:** Searching in sorted arrays  
**Real-world Use Cases:**
- Database indexing
- Dictionary lookups
- Finding version in sorted release history
- Debugging with git bisect

**When NOT to use:** Unsorted data, linked lists, small datasets (<10 elements)

---

### Linear Search
**Time Complexity:** O(n)  
**Space Complexity:** O(1)  
**Best For:** Small or unsorted datasets  
**Real-world Use Cases:**
- Finding element in unsorted array
- Searching linked lists
- Small datasets where overhead of sorting isn't worth it
- When you need to find ALL occurrences

**When NOT to use:** Large sorted datasets (use binary search instead)

---

## 🔄 Sorting Algorithms

### Bubble Sort
**Time Complexity:** O(n²) average/worst, O(n) best  
**Space Complexity:** O(1)  
**Stable:** Yes  
**Real-world Use Cases:**
- Educational purposes
- Nearly sorted data
- Small datasets (<50 elements)
- Hardware with limited memory

**When NOT to use:** Large datasets, production systems

---

### Merge Sort
**Time Complexity:** O(n log n) all cases  
**Space Complexity:** O(n)  
**Stable:** Yes  
**Real-world Use Cases:**
- External sorting (files too large for memory)
- Sorting linked lists
- When stability is required
- Parallel processing (divide and conquer)
- Database sorting operations

**When NOT to use:** Memory-constrained environments, small datasets

---

### Quick Sort
**Time Complexity:** O(n log n) average, O(n²) worst  
**Space Complexity:** O(log n)  
**Stable:** No  
**Real-world Use Cases:**
- General-purpose sorting (most languages' default)
- In-memory sorting
- When average case performance matters
- Cache-friendly operations

**When NOT to use:** When worst-case O(n²) is unacceptable, need stability

---

### Heap Sort
**Time Complexity:** O(n log n) all cases  
**Space Complexity:** O(1)  
**Stable:** No  
**Real-world Use Cases:**
- Memory-constrained systems
- Real-time systems (predictable performance)
- Priority queue implementation
- When in-place sorting is required

**When NOT to use:** When stability needed, cache performance critical

---

## 🌐 Graph Algorithms

### Depth-First Search (DFS)
**Time Complexity:** O(V + E)  
**Space Complexity:** O(V)  
**Real-world Use Cases:**
- Maze solving
- Topological sorting
- Detecting cycles
- Path finding in games
- Web crawling
- Dependency resolution

**When NOT to use:** Finding shortest path (use BFS)

---

### Breadth-First Search (BFS)
**Time Complexity:** O(V + E)  
**Space Complexity:** O(V)  
**Real-world Use Cases:**
- Shortest path in unweighted graphs
- Social network connections (degrees of separation)
- GPS navigation
- Network broadcasting
- Peer-to-peer networks

**When NOT to use:** Weighted graphs (use Dijkstra), deep graphs (memory intensive)

---

### Dijkstra's Algorithm
**Time Complexity:** O((V + E) log V) with priority queue  
**Space Complexity:** O(V)  
**Real-world Use Cases:**
- GPS navigation and routing
- Network routing protocols (OSPF)
- Flight route optimization
- Game pathfinding
- Social network analysis

**When NOT to use:** Negative edge weights (use Bellman-Ford), all-pairs shortest path (use Floyd-Warshall)

---

### Topological Sort
**Time Complexity:** O(V + E)  
**Space Complexity:** O(V)  
**Real-world Use Cases:**
- Build systems (dependency resolution)
- Course prerequisite scheduling
- Task scheduling with dependencies
- Package manager dependency resolution
- Spreadsheet formula evaluation

**When NOT to use:** Graphs with cycles (not a DAG)

---

## 🏗️ Data Structures

### Hash Table
**Time Complexity:** O(1) average for insert/delete/search  
**Space Complexity:** O(n)  
**Real-world Use Cases:**
- Database indexing
- Caching (LRU cache)
- Symbol tables in compilers
- Counting frequencies
- Removing duplicates
- Dictionary implementations

**When NOT to use:** Need ordered data, range queries, memory very limited

---

### Binary Search Tree (BST)
**Time Complexity:** O(log n) average, O(n) worst  
**Space Complexity:** O(n)  
**Real-world Use Cases:**
- Database indexing (B-trees)
- File systems
- Expression parsing
- Auto-complete features
- Range queries

**When NOT to use:** Unbalanced trees (use AVL/Red-Black), need O(1) lookup (use hash table)

---

### Linked List
**Time Complexity:** O(1) insert/delete at head, O(n) search  
**Space Complexity:** O(n)  
**Real-world Use Cases:**
- Implementing stacks and queues
- Undo functionality
- Music playlists
- Browser history
- Memory management (free lists)

**When NOT to use:** Need random access, memory overhead is concern

---

### Trie
**Time Complexity:** O(m) where m is key length  
**Space Complexity:** O(ALPHABET_SIZE × N × M)  
**Real-world Use Cases:**
- Auto-complete/type-ahead
- Spell checkers
- IP routing tables
- Dictionary implementations
- DNA sequence analysis

**When NOT to use:** Memory constrained, small datasets (hash table better)

---

## 🧮 Dynamic Programming

### Fibonacci
**Time Complexity:** O(n) with DP, O(2ⁿ) naive  
**Space Complexity:** O(n) or O(1) optimized  
**Real-world Use Cases:**
- Algorithm optimization teaching
- Financial modeling
- Population growth models
- Spiral patterns in nature

---

### Knapsack Problem
**Time Complexity:** O(n × W)  
**Space Complexity:** O(n × W)  
**Real-world Use Cases:**
- Resource allocation
- Budget optimization
- Cargo loading
- Portfolio optimization
- Memory management

**When NOT to use:** Fractional items allowed (use greedy), very large capacity

---

### Edit Distance (Levenshtein)
**Time Complexity:** O(m × n)  
**Space Complexity:** O(m × n)  
**Real-world Use Cases:**
- Spell checkers
- DNA sequence alignment
- Plagiarism detection
- Fuzzy string matching
- Version control diffs

---

### Longest Common Subsequence (LCS)
**Time Complexity:** O(m × n)  
**Space Complexity:** O(m × n)  
**Real-world Use Cases:**
- Diff tools (git diff)
- DNA sequence comparison
- File comparison utilities
- Plagiarism detection
- Data deduplication

---

### Coin Change
**Time Complexity:** O(n × amount)  
**Space Complexity:** O(amount)  
**Real-world Use Cases:**
- Making change optimally
- Currency exchange
- Resource allocation
- Vending machines
- Payment systems

---

## 🔤 String Algorithms

### KMP (Knuth-Morris-Pratt)
**Time Complexity:** O(n + m)  
**Space Complexity:** O(m)  
**Real-world Use Cases:**
- Text editors (find/replace)
- DNA sequence matching
- Plagiarism detection
- Network intrusion detection
- Log file analysis

**When NOT to use:** Single search (simple search fine), multiple patterns (use Aho-Corasick)

---

### Palindrome Check
**Time Complexity:** O(n)  
**Space Complexity:** O(1)  
**Real-world Use Cases:**
- Data validation
- DNA sequence analysis
- Compression algorithms
- Cryptography
- String manipulation puzzles

---

## 📊 Mathematical Algorithms

### Euclidean Algorithm (GCD)
**Time Complexity:** O(log min(a,b))  
**Space Complexity:** O(1)  
**Real-world Use Cases:**
- Fraction simplification
- Cryptography (RSA)
- Music theory (rhythm patterns)
- Computer graphics (aspect ratios)
- Modular arithmetic

---

### Sieve of Eratosthenes
**Time Complexity:** O(n log log n)  
**Space Complexity:** O(n)  
**Real-world Use Cases:**
- Prime number generation
- Cryptography
- Hash functions
- Number theory research
- Competitive programming

**When NOT to use:** Single prime check (use primality test), very large n (memory)

---

### Matrix Multiplication
**Time Complexity:** O(n³) naive, O(n^2.807) Strassen  
**Space Complexity:** O(n²)  
**Real-world Use Cases:**
- Computer graphics transformations
- Machine learning (neural networks)
- Scientific computing
- Image processing
- Physics simulations

---

## 🤖 Machine Learning Algorithms

### Linear Regression
**Time Complexity:** O(n) per iteration  
**Space Complexity:** O(n)  
**Real-world Use Cases:**
- Price prediction
- Sales forecasting
- Risk assessment
- Trend analysis
- Simple predictive models

---

### Logistic Regression
**Time Complexity:** O(n × iterations)  
**Space Complexity:** O(n)  
**Real-world Use Cases:**
- Binary classification
- Spam detection
- Disease diagnosis
- Credit scoring
- Click-through rate prediction

---

### Decision Trees
**Time Complexity:** O(n log n) training, O(log n) prediction  
**Space Complexity:** O(n)  
**Real-world Use Cases:**
- Customer segmentation
- Medical diagnosis
- Credit approval
- Fraud detection
- Feature importance analysis

---

### Random Forest
**Time Complexity:** O(n log n × trees)  
**Space Complexity:** O(n × trees)  
**Real-world Use Cases:**
- Robust classification
- Feature selection
- Anomaly detection
- Recommendation systems
- Risk assessment

---

### Support Vector Machines (SVM)
**Time Complexity:** O(n²) to O(n³)  
**Space Complexity:** O(n)  
**Real-world Use Cases:**
- Image classification
- Text categorization
- Handwriting recognition
- Bioinformatics
- Face detection

---

### K-Means Clustering
**Time Complexity:** O(n × k × iterations)  
**Space Complexity:** O(n + k)  
**Real-world Use Cases:**
- Customer segmentation
- Image compression
- Document clustering
- Anomaly detection
- Market research

---

### K-Nearest Neighbors (KNN)
**Time Complexity:** O(n) per query  
**Space Complexity:** O(n)  
**Real-world Use Cases:**
- Recommendation systems
- Pattern recognition
- Credit rating
- Image recognition
- Medical diagnosis

---

### Gradient Boosting
**Time Complexity:** O(n × trees × depth)  
**Space Complexity:** O(n × trees)  
**Real-world Use Cases:**
- Kaggle competitions
- Click-through rate prediction
- Risk modeling
- Ranking problems
- High-accuracy predictions

---

## 🎯 Algorithm Selection Guide

### By Problem Type:
- **Searching:** Binary Search (sorted), Linear Search (unsorted)
- **Sorting:** Quick Sort (general), Merge Sort (stable), Heap Sort (in-place)
- **Shortest Path:** Dijkstra (weighted), BFS (unweighted)
- **Pattern Matching:** KMP (single pattern), Trie (multiple patterns)
- **Optimization:** Dynamic Programming (overlapping subproblems)

### By Constraints:
- **Memory Limited:** Heap Sort, In-place Quick Sort
- **Time Critical:** Hash Table, Binary Search
- **Stability Required:** Merge Sort, Bubble Sort
- **Worst-case Guarantee:** Merge Sort, Heap Sort

### By Data Characteristics:
- **Nearly Sorted:** Insertion Sort, Bubble Sort
- **Small Dataset:** Simple algorithms (Linear Search, Bubble Sort)
- **Large Dataset:** Efficient algorithms (Quick Sort, Hash Table)
- **Streaming Data:** Online algorithms, Sliding Window

---

## 📖 Further Reading

- **Books:** "Introduction to Algorithms" (CLRS), "Algorithm Design Manual" (Skiena)
- **Online:** LeetCode, HackerRank, Codeforces
- **Visualization:** VisuAlgo, Algorithm Visualizer
- **Practice:** Project Euler, Advent of Code

---

**Last Updated:** October 2025  
**Maintained by:** Vitor Hansen
