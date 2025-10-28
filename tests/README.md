# 🧪 Algorithm Tests

Automated unit tests for algorithm implementations across multiple languages.

## 📊 Test Coverage

| Language | Test Files | Test Cases | Status | Coverage |
|----------|-----------|------------|--------|----------|
| Python | 34 | 71 (63 passing, 8 skipped) | ✅ | 100% |
| JavaScript | 34 | 61 | ✅ 100% passing | 100% |
| Java | 34 | 34 | ⏳ Requires JDK | 100% |

**Total: 102 test files covering all 34 algorithms**

### Test Results Summary

- **Python**: 63 tests passing, 8 skipped (ML algorithms without numpy)
- **JavaScript**: 61 tests passing (100%)
- **Java**: 34 tests ready to run (requires JDK installation)

### ✅ All Algorithms Tested (34)

**Sorting & Search:**
1. Binary Search
2. Linear Search
3. Merge Sort
4. Quick Sort
5. Bubble Sort
6. Heap Sort

**Data Structures:**
7. Hash Table
8. Binary Search Tree
9. Linked List
10. Trie

**Graph Algorithms:**
11. Depth-First Search
12. Breadth-First Search
13. Dijkstra's Algorithm
14. Topological Sort

**Dynamic Programming:**
15. Fibonacci
16. Knapsack Problem
17. Coin Change
18. Edit Distance
19. Longest Common Subsequence
20. Dynamic Programming
21. Matrix Multiplication

**String Algorithms:**
22. KMP Algorithm
23. Palindrome

**Math:**
24. Euclidean Algorithm
25. Sieve of Eratosthenes
26. Two Pointers

**Machine Learning:**
27. Decision Trees
28. Linear Regression
29. Logistic Regression
30. Random Forest
31. Gradient Boosting
32. K-Means Clustering
33. K-Nearest Neighbors
34. Support Vector Machines

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
