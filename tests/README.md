# 🧪 Algorithm Tests

Automated unit tests for algorithm implementations across multiple languages.

## 📊 Test Coverage

| Language | Algorithms Tested | Status |
|----------|------------------|--------|
| Python | Binary Search, Merge Sort, Hash Table | ✅ |
| JavaScript | Binary Search, Merge Sort | ✅ |
| Java | Binary Search | ✅ |

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
