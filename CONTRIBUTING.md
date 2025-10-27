# Contributing to Multi-Language Algorithm Library

Thank you for your interest in contributing to this project! This guide will help you get started.

## 🎯 Project Goals

- Maintain **consistent implementations** across all 13 languages
- Provide **educational value** with clear, readable code
- Ensure **correctness** and **efficiency** of algorithms
- Keep implementations **minimal but complete**

## 🔧 Development Setup

1. **Fork** the repository
2. **Clone** your fork locally
3. **Create** a new branch for your feature
4. **Make** your changes
5. **Test** your implementations
6. **Submit** a pull request

## 📝 Implementation Guidelines

### Code Style
- Follow language-specific conventions
- Use clear, descriptive variable names
- Include comments for complex logic
- Keep implementations concise but readable

### File Naming
- Use consistent naming across languages
- Follow existing patterns in the repository
- For classes: `AlgorithmName.java`, `AlgorithmName.kt`
- For scripts: `algorithm_name.py`, `algorithm_name.js`

### Testing
- Include a simple test case in each implementation
- Verify correctness with known inputs/outputs
- Test edge cases where applicable

## 🆕 Adding New Algorithms

When adding a new algorithm:

1. **Create directory**: `algorithm-name/`
2. **Implement in all 13 languages**:
   - C (`.c`)
   - C++ (`.cpp`)
   - C# (`.cs`)
   - Clojure (`.clj`)
   - Go (`.go`)
   - Java (`.java`)
   - JavaScript (`.js`)
   - Kotlin (`.kt`)
   - PHP (`.php`)
   - Python (`.py`)
   - Ruby (`.rb`)
   - Rust (`.rs`)
   - TypeScript (`.ts`)

3. **Update README.md** with:
   - Algorithm description
   - Time/space complexity
   - Use cases
   - Link to directory

### Algorithm Template

Each implementation should follow this structure:

```python
# Python example
def algorithm_name(input_data):
    """
    Brief description of what the algorithm does.
    
    Args:
        input_data: Description of input
        
    Returns:
        Description of output
    """
    # Implementation here
    pass

# Test case
if __name__ == "__main__":
    test_input = [1, 2, 3, 4, 5]
    result = algorithm_name(test_input)
    print(f"Result: {result}")
```

## 🐛 Bug Reports

When reporting bugs:

1. **Describe** the issue clearly
2. **Specify** which language implementation
3. **Provide** input that causes the problem
4. **Include** expected vs actual output

## 💡 Feature Requests

For new features:

1. **Check** existing issues first
2. **Describe** the algorithm/feature
3. **Explain** why it would be valuable
4. **Consider** implementation complexity

## 🔍 Code Review Process

All contributions go through code review:

1. **Automated checks** for basic issues
2. **Manual review** for correctness and style
3. **Testing** across multiple languages
4. **Documentation** updates if needed

## 📋 Checklist for Pull Requests

- [ ] Algorithm implemented in all 13 languages
- [ ] Each implementation includes test case
- [ ] Code follows language conventions
- [ ] README.md updated with algorithm info
- [ ] All files follow naming conventions
- [ ] No compilation/runtime errors

## 🎓 Learning Resources

If you're new to any of the languages:

- **C/C++**: [Learn C++](https://www.learncpp.com/)
- **Java**: [Oracle Java Tutorials](https://docs.oracle.com/javase/tutorial/)
- **Python**: [Python.org Tutorial](https://docs.python.org/3/tutorial/)
- **JavaScript**: [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- **Rust**: [The Rust Book](https://doc.rust-lang.org/book/)
- **Go**: [Tour of Go](https://tour.golang.org/)

## 🤝 Community Guidelines

- Be respectful and constructive
- Help others learn and improve
- Focus on code quality and education
- Ask questions if you're unsure

## 📞 Getting Help

- **Issues**: For bugs and feature requests
- **Discussions**: For questions and general discussion
- **Code Review**: For implementation feedback

Thank you for contributing to make this a valuable resource for the programming community! 🚀
