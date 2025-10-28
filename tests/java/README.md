# Java Tests

## Prerequisites

Install Java Development Kit (JDK):
```bash
# macOS
brew install openjdk

# Ubuntu/Debian
sudo apt install default-jdk

# Windows
# Download from https://www.oracle.com/java/technologies/downloads/
```

## Running Tests

Run all tests:
```bash
bash run_tests.sh
```

Run individual test:
```bash
javac -cp ../../binary-search/ BinarySearchTest.java
java -ea -cp ../../binary-search/:. BinarySearchTest
```

## Test Coverage

34 tests covering all algorithms:
- **Sorting**: Bubble, Quick, Merge, Heap
- **Search**: Binary, Linear
- **Data Structures**: BST, Hash Table, Linked List, Trie
- **Graph**: DFS, BFS, Topological Sort, Dijkstra
- **Dynamic Programming**: Knapsack, Coin Change, Edit Distance, LCS, DP
- **String**: KMP, Palindrome
- **Math**: Fibonacci, Euclidean, Sieve, Matrix Multiplication, Two Pointers
- **Machine Learning**: Decision Tree, Linear Regression, Logistic Regression, Random Forest, Gradient Boosting, K-Means, KNN, SVM
