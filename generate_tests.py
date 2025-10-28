#!/usr/bin/env python3
"""
Automatic test generator for all algorithms
Generates basic test files for Python, JavaScript, and Java

Usage:
    python3 generate_tests.py

This will generate test files for algorithms defined in the ALGORITHMS dict.
Tests are only generated if they don't already exist.

To regenerate a test, delete it first:
    rm tests/python/test_algorithm_name.py
    python3 generate_tests.py

Note: Some algorithms may need manual adjustment if they have:
- Different function signatures
- Multiple function variants
- Special input/output formats
"""

import os
from pathlib import Path

# Algorithm configurations with test cases
ALGORITHMS = {
    'binary-search': {
        'function': 'binary_search',
        'tests': [
            (['1, 2, 3, 4, 5'], '3', '2'),
            (['1, 2, 3, 4, 5'], '1', '0'),
            (['1, 2, 3, 4, 5'], '6', '-1'),
            ('[]', '1', '-1'),
        ]
    },
    'linear-search': {
        'function': 'linear_search',
        'tests': [
            (['3, 1, 4, 1, 5'], '4', '2'),
            (['3, 1, 4, 1, 5'], '9', '-1'),
            ('[]', '1', '-1'),
        ]
    },
    'merge-sort': {
        'function': 'merge_sort',
        'tests': [
            (['5, 4, 3, 2, 1'], None, '[1, 2, 3, 4, 5]'),
            (['1, 2, 3, 4, 5'], None, '[1, 2, 3, 4, 5]'),
            ('[]', None, '[]'),
        ]
    },
    'quick-sort': {
        'function': 'quick_sort',
        'tests': [
            (['5, 4, 3, 2, 1'], None, '[1, 2, 3, 4, 5]'),
            (['3, 1, 4, 1, 5'], None, '[1, 1, 3, 4, 5]'),
        ]
    },
    'bubble-sort': {
        'function': 'bubble_sort',
        'tests': [
            (['5, 4, 3, 2, 1'], None, '[1, 2, 3, 4, 5]'),
            (['1, 2, 3'], None, '[1, 2, 3]'),
        ]
    },
    'heap-sort': {
        'function': 'heap_sort',
        'tests': [
            (['5, 4, 3, 2, 1'], None, '[1, 2, 3, 4, 5]'),
        ]
    },
    'fibonacci': {
        'function': 'fibonacci_iterative',
        'tests': [
            (None, '0', '0'),
            (None, '1', '1'),
            (None, '5', '5'),
            (None, '10', '55'),
        ]
    },
    'palindrome': {
        'function': 'is_palindrome_simple',
        'tests': [
            (None, '"racecar"', 'True'),
            (None, '"hello"', 'False'),
            (None, '""', 'True'),
        ]
    },
}

def generate_python_test(algo_name, config):
    """Generate Python pytest file"""
    func_name = config['function']
    file_name = algo_name.replace('-', '_')
    
    test_code = f'''import sys
import os
import importlib.util
import glob

# Load algorithm implementation
algo_dir = os.path.join(os.path.dirname(__file__), '../../{algo_name}')
sys.path.insert(0, algo_dir)

# Try different file naming conventions
py_files = glob.glob(os.path.join(algo_dir, '*.py'))
if not py_files:
    raise FileNotFoundError(f"No Python file found in {{algo_dir}}")

spec = importlib.util.spec_from_file_location("{file_name}", py_files[0])
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Try to get the function
try:
    {func_name} = getattr(module, '{func_name}')
except AttributeError:
    # Try alternative names
    for attr in dir(module):
        if attr.lower().replace('_', '') == '{func_name}'.lower().replace('_', ''):
            {func_name} = getattr(module, attr)
            break
    else:
        raise AttributeError(f"Function '{func_name}' not found in module")

'''
    
    for i, test in enumerate(config['tests'], 1):
        arr, arg, expected = test
        test_code += f'''def test_case_{i}():
'''
        if arr:
            test_code += f'''    arr = [{arr}]
    assert {func_name}(arr, {arg}) == {expected}

'''
        else:
            test_code += f'''    assert {func_name}({arg}) == {expected}

'''
    
    return test_code

def generate_javascript_test(algo_name, config):
    """Generate JavaScript Jest test file"""
    func_name = config['function']
    file_name = algo_name.replace('_', '-')
    
    test_code = f'''const fs = require('fs');
const path = require('path');

// Load implementation
const algoPath = path.join(__dirname, '../../{algo_name}/{file_name}.js');
const code = fs.readFileSync(algoPath, 'utf8');
eval(code);

describe('{algo_name.replace("-", " ").title()}', () => {{
'''
    
    for i, test in enumerate(config['tests'], 1):
        arr, arg, expected = test
        test_code += f'''  test('test case {i}', () => {{
'''
        if arr:
            test_code += f'''    expect({func_name}([{arr}], {arg})).toBe({expected});
'''
        else:
            test_code += f'''    expect({func_name}({arg})).toBe({expected});
'''
        test_code += f'''  }});

'''
    
    test_code += '});\n'
    return test_code

def main():
    base_dir = Path(__file__).parent
    tests_dir = base_dir / 'tests'
    
    print("🧪 Generating tests for all algorithms...\n")
    
    generated = {'python': 0, 'javascript': 0}
    
    for algo_name, config in ALGORITHMS.items():
        # Check if algorithm directory exists
        algo_dir = base_dir / algo_name
        if not algo_dir.exists():
            print(f"⚠️  Skipping {algo_name} (directory not found)")
            continue
        
        # Generate Python test
        py_test_file = tests_dir / 'python' / f'test_{algo_name.replace("-", "_")}.py'
        if not py_test_file.exists():
            py_test_file.write_text(generate_python_test(algo_name, config))
            print(f"✅ Generated Python test: {py_test_file.name}")
            generated['python'] += 1
        
        # Generate JavaScript test
        js_test_file = tests_dir / 'javascript' / f'{algo_name.replace("-", "")}.test.js'
        if not js_test_file.exists():
            js_test_file.write_text(generate_javascript_test(algo_name, config))
            print(f"✅ Generated JavaScript test: {js_test_file.name}")
            generated['javascript'] += 1
    
    print(f"\n📊 Summary:")
    print(f"   Python tests generated: {generated['python']}")
    print(f"   JavaScript tests generated: {generated['javascript']}")
    print(f"\n🚀 Run tests with:")
    print(f"   cd tests/python && pytest -v")
    print(f"   cd tests/javascript && npm test")

if __name__ == '__main__':
    main()
