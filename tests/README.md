# 🧪 Algorithm Tests

Automated unit tests for algorithm implementations across multiple languages.

# 🧪 Algorithm Tests

Automated unit tests for algorithm implementations across multiple languages.

## 📊 Test Coverage

| Language | Algorithms Tested | Tests Passing | Coverage |
|----------|------------------|---------------|----------|
| Python | 21 of 34 | 58/58 ✅ | 62% |
| JavaScript | 21 of 34 | 14/14 ✅ | 62% |
| Java | 1 of 34 | 5/5 ✅ | 3% |

### ✅ Tested Algorithms (21)

1. Binary Search
2. Linear Search
3. Merge Sort
4. Quick Sort
5. Bubble Sort
6. Heap Sort
7. Hash Table
8. Fibonacci
9. Palindrome
10. Euclidean Algorithm
11. Depth-First Search
12. Breadth-First Search
13. Coin Change
14. Edit Distance
15. Knapsack Problem
16. Longest Common Subsequence
17. Matrix Multiplication
18. Sieve of Eratosthenes
19. Two Pointers
20. KMP Algorithm
21. Dynamic Programming

### ⏭️ Algorithms Requiring Manual Tests (13)

These algorithms require class instantiation, training data, or complex setup:

- Binary Search Tree (class-based)
- Linked List (class-based)
- Trie (class-based)
- Dijkstra's Algorithm (complex graph structure)
- Topological Sort (complex graph structure)
- Linear Regression (requires numpy/training)
- Logistic Regression (requires numpy/training)
- Decision Trees (requires class/training)
- Random Forest (requires class/training)
- Support Vector Machines (requires class/training)
- K-Means Clustering (requires numpy)
- K-Nearest Neighbors (requires numpy)
- Gradient Boosting (requires class/training)

## 🚀 Running Tests

### Python
```bash
cd tests/python
pip install pytest
pytest -v
```

Or use the script:
```bash
./tests/python/run_tests.sh
```

### JavaScript
```bash
cd tests/javascript
npm install
npm test
```

### Java
```bash
cd tests/java
./run_tests.sh
```

## 🔄 Continuous Integration

Tests run automatically on every push and pull request via GitHub Actions.

See `.github/workflows/test.yml` for the CI configuration.

## 📝 Adding New Tests

### Python
Create a new file `test_<algorithm>.py` in `tests/python/`:

```python
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../<algorithm-folder>'))

from <algorithm_file> import <function_name>

def test_case_1():
    assert <function_name>(input) == expected_output
```

### JavaScript
Create a new file `<algorithm>.test.js` in `tests/javascript/`:

```javascript
const fs = require('fs');
const path = require('path');

const algorithmPath = path.join(__dirname, '../../<algorithm-folder>/<file>.js');
const code = fs.readFileSync(algorithmPath, 'utf8');
eval(code);

describe('<Algorithm Name>', () => {
  test('test case description', () => {
    expect(functionName(input)).toBe(expectedOutput);
  });
});
```

### Java
Add test methods to the appropriate test class or create a new one following the pattern in `BinarySearchTest.java`.

## 🎯 Future Improvements

- [ ] Add tests for C++ implementations
- [ ] Add tests for Go implementations
- [ ] Add tests for Rust implementations
- [ ] Increase test coverage to all 34 algorithms
- [ ] Add performance benchmarks
- [ ] Add code coverage reports

## 📖 Test Frameworks Used

- **Python:** pytest
- **JavaScript:** Jest
- **Java:** Custom test runner (can be upgraded to JUnit)

---

**Maintained by:** Vitor Hansen  
**Last Updated:** October 2025
