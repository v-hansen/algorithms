# 🚀 Multi-Language Algorithm Library

[![Algorithms](https://img.shields.io/badge/algorithms-34-blue.svg)](./ALGORITHMS.md)
[![Languages](https://img.shields.io/badge/languages-13-green.svg)](#-supported-languages)
[![Implementations](https://img.shields.io/badge/implementations-442-orange.svg)](#-project-overview)
[![License](https://img.shields.io/badge/license-MIT-purple.svg)](./LICENSE)
[![Completion](https://img.shields.io/badge/completion-100%25-brightgreen.svg)](#-project-overview)

A comprehensive collection of **34 fundamental algorithms** implemented in **13 programming languages**. This repository serves as both a learning resource and a practical reference for algorithm implementations across different programming paradigms.

## 📊 Project Overview

- **34 Algorithms** × **13 Languages** = **442 Implementations**
- **100% Consistent** structure across all languages
- **Production-ready** code with examples
- **Educational** comments and documentation

## 🔧 Supported Languages

| Language | Extension | Paradigm |
|----------|-----------|----------|
| C | `.c` | Procedural |
| C++ | `.cpp` | Object-Oriented/Generic |
| C# | `.cs` | Object-Oriented |
| Clojure | `.clj` | Functional |
| Go | `.go` | Concurrent |
| Java | `.java` | Object-Oriented |
| JavaScript | `.js` | Multi-paradigm |
| Kotlin | `.kt` | Multi-paradigm |
| PHP | `.php` | Web-focused |
| Python | `.py` | Multi-paradigm |
| Ruby | `.rb` | Object-Oriented |
| Rust | `.rs` | Systems |
| TypeScript | `.ts` | Typed JavaScript |

## 📚 Algorithm Categories

> 💡 **See [ALGORITHMS.md](./ALGORITHMS.md) for detailed complexity analysis, use cases, and implementation notes for each algorithm.**
> 
> 📊 **See [DIAGRAMS.md](./DIAGRAMS.md) for visual flowcharts and decision trees.**

### 🔍 **Search & Basic Algorithms**
| Algorithm | Time Complexity | Space Complexity | Use Case |
|-----------|----------------|------------------|----------|
| [Binary Search](./binary-search/) | O(log n) | O(1) | Searching in sorted arrays |
| [Linear Search](./linear-search/) | O(n) | O(1) | Searching in unsorted arrays |
| [Two Pointers](./two_pointers/) | O(n) | O(1) | Array problems, pair finding |

### 🔄 **Sorting Algorithms**
| Algorithm | Time Complexity | Space Complexity | Stability | Use Case |
|-----------|----------------|------------------|-----------|----------|
| [Bubble Sort](./bubble-sort/) | O(n²) | O(1) | Stable | Educational, small datasets |
| [Merge Sort](./merge-sort/) | O(n log n) | O(n) | Stable | Large datasets, external sorting |
| [Quick Sort](./quick-sort/) | O(n log n) avg, O(n²) worst | O(log n) | Unstable | General purpose, in-place sorting |
| [Heap Sort](./heap-sort/) | O(n log n) | O(1) | Unstable | Memory-constrained environments |

### 🤖 **Machine Learning Algorithms**
| Algorithm | Time Complexity | Space Complexity | Type | Use Case |
|-----------|----------------|------------------|------|----------|
| [Linear Regression](./linear-regression/) | O(n) | O(1) | Supervised | Continuous prediction |
| [Logistic Regression](./logistic-regression/) | O(n×iterations) | O(n) | Supervised | Binary classification |
| [Decision Trees](./decision-trees/) | O(n log n) | O(n) | Supervised | Classification/Regression |
| [Random Forest](./random-forest/) | O(n log n × trees) | O(n × trees) | Ensemble | Robust classification |
| [Support Vector Machines](./support-vector-machines/) | O(n²) to O(n³) | O(n) | Supervised | High-dimensional classification |
| [K-Means Clustering](./k-means-clustering/) | O(n×k×iterations) | O(n+k) | Unsupervised | Data clustering |
| [K-Nearest Neighbors](./k-nearest-neighbors/) | O(n) per query | O(n) | Lazy Learning | Classification/Regression |
| [Gradient Boosting](./gradient-boosting/) | O(n×trees×depth) | O(n×trees) | Ensemble | High-accuracy prediction |

### 🌐 **Graph Algorithms**
| Algorithm | Time Complexity | Space Complexity | Use Case |
|-----------|----------------|------------------|----------|
| [Depth-First Search](./depth-first-search/) | O(V + E) | O(V) | Graph traversal, pathfinding |
| [Breadth-First Search](./breadth-first-search/) | O(V + E) | O(V) | Shortest path, level-order traversal |
| [Dijkstra's Algorithm](./dijkstra-algorithm/) | O((V + E) log V) | O(V) | Shortest path in weighted graphs |
| [Topological Sort](./topological-sort/) | O(V + E) | O(V) | Dependency resolution, scheduling |

### 🏗️ **Data Structures**
| Structure | Access | Search | Insertion | Deletion | Use Case |
|-----------|--------|--------|-----------|----------|----------|
| [Hash Table](./hash-table/) | O(1) avg | O(1) avg | O(1) avg | O(1) avg | Fast key-value storage |
| [Binary Search Tree](./binary-search-tree/) | O(log n) avg | O(log n) avg | O(log n) avg | O(log n) avg | Ordered data storage |
| [Linked List](./linked-list/) | O(n) | O(n) | O(1) | O(1) | Dynamic size, frequent insertions |
| [Trie](./trie/) | O(m) | O(m) | O(m) | O(m) | String prefix operations |

### 🧮 **Dynamic Programming**
| Algorithm | Time Complexity | Space Complexity | Technique | Use Case |
|-----------|----------------|------------------|-----------|----------|
| [Dynamic Programming](./dynamic-programming/) | Varies | Varies | Memoization/Tabulation | Optimization problems |
| [Knapsack Problem](./knapsack-problem/) | O(n×W) | O(n×W) | 2D DP | Resource allocation |
| [Edit Distance](./edit-distance/) | O(m×n) | O(m×n) | 2D DP | String similarity |
| [Longest Common Subsequence](./longest-common-subsequence/) | O(m×n) | O(m×n) | 2D DP | Sequence alignment |
| [Coin Change](./coin-change/) | O(n×amount) | O(amount) | 1D DP | Making change optimally |

### 🔤 **String Algorithms**
| Algorithm | Time Complexity | Space Complexity | Use Case |
|-----------|----------------|------------------|----------|
| [KMP Algorithm](./kmp-algorithm/) | O(n + m) | O(m) | Pattern matching |
| [Palindrome](./palindrome/) | O(n) | O(1) | String validation |

### 📊 **Mathematical Algorithms**
| Algorithm | Time Complexity | Space Complexity | Use Case |
|-----------|----------------|------------------|----------|
| [Fibonacci](./fibonacci/) | O(n) | O(1) | Mathematical sequences |
| [Euclidean Algorithm](./euclidean-algorithm/) | O(log min(a,b)) | O(1) | Greatest Common Divisor |
| [Sieve of Eratosthenes](./sieve-of-eratosthenes/) | O(n log log n) | O(n) | Prime number generation |
| [Matrix Multiplication](./matrix-multiplication/) | O(n³) | O(n²) | Linear algebra operations |
| [Fibonacci](./fibonacci/) | O(n) | O(1) | Mathematical sequences |
| [Palindrome](./palindrome/) | O(n) | O(1) | String validation |

## 🚀 Quick Start

### Clone the Repository
```bash
git clone https://github.com/yourusername/multi-language-algorithms.git
cd multi-language-algorithms
```

### Run Examples

#### Python
```bash
cd linear-regression
python linear_regression.py
```

#### JavaScript
```bash
cd merge-sort
node merge_sort.js
```

#### Java
```bash
cd quick-sort
javac QuickSort.java
java QuickSort
```

#### C++
```bash
cd binary-search-tree
g++ binary_search_tree.cpp -o bst
./bst
```

## 📁 Project Structure

```
├── README.md
├── binary-search/
│   ├── binary_search.py
│   ├── binary_search.js
│   ├── BinarySearch.java
│   └── ... (13 implementations)
├── merge-sort/
│   ├── merge_sort.py
│   ├── merge_sort.js
│   ├── MergeSort.java
│   └── ... (13 implementations)
└── ... (21 algorithm directories)
```

Each algorithm directory contains:
- **Consistent naming** across languages
- **Working examples** with test data
- **Minimal but complete** implementations
- **Educational comments** where helpful

## 🎯 Algorithm Selection Guide

### **For Learning:**
- Start with **Bubble Sort** and **Linear Search**
- Progress to **Merge Sort** and **Binary Search**
- Explore **DFS/BFS** for graph concepts

### **For Interviews:**
- **Two Pointers** technique
- **Dynamic Programming** patterns
- **Tree/Graph traversals**

### **For Production:**
- **Quick Sort** for general sorting
- **Hash Tables** for fast lookups
- **Dijkstra** for pathfinding

### **For Data Science:**
- **Linear/Logistic Regression** for baselines
- **Random Forest** for robust models
- **K-Means** for clustering

## 🔬 Complexity Analysis

### Time Complexity Classes
- **O(1)** - Constant: Hash table operations
- **O(log n)** - Logarithmic: Binary search, balanced trees
- **O(n)** - Linear: Linear search, array traversal
- **O(n log n)** - Linearithmic: Efficient sorting algorithms
- **O(n²)** - Quadratic: Simple sorting, nested loops
- **O(2ⁿ)** - Exponential: Recursive algorithms without memoization

### Space Complexity Considerations
- **In-place algorithms**: O(1) extra space
- **Recursive algorithms**: O(depth) stack space
- **Dynamic programming**: O(n) for memoization tables

## 🛠️ Implementation Standards

### Code Quality
- ✅ **Consistent style** across languages
- ✅ **Error handling** where appropriate
- ✅ **Test cases** included
- ✅ **Documentation** in code

### Performance
- ✅ **Optimal algorithms** chosen for each use case
- ✅ **Language-specific optimizations**
- ✅ **Memory-efficient** implementations

## 🤝 Contributing

1. **Fork** the repository
2. **Create** a feature branch
3. **Implement** the algorithm in all 13 languages
4. **Test** all implementations
5. **Submit** a pull request

### Adding New Algorithms
- Follow the existing directory structure
- Implement in all 13 languages
- Include test cases and documentation
- Update this README

## 📖 Educational Resources

### Books
- "Introduction to Algorithms" by Cormen, Leiserson, Rivest, and Stein
- "Algorithm Design Manual" by Steven Skiena
- "Hands-On Machine Learning" by Aurélien Géron

### Online Courses
- MIT 6.006 Introduction to Algorithms
- Stanford CS161 Design and Analysis of Algorithms
- Coursera Machine Learning Course

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Acknowledgments

- **Computer Science Community** for algorithm development
- **Open Source Contributors** for language implementations
- **Educational Institutions** for algorithmic foundations

## 📊 Statistics

- **Total Files**: 403
- **Total Lines of Code**: ~25,000+
- **Languages Covered**: 13
- **Algorithm Categories**: 8
- **Complexity Classes**: All major classes covered

---

**⭐ Star this repository if you find it helpful!**

**🔗 Share with fellow developers and students!**

**📚 Use for learning, teaching, and reference!**
