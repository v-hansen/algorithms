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
    'euclidean-algorithm': {
        'function': 'gcd',
        'tests': [
            (None, '48, 18', '6'),
            (None, '100, 50', '50'),
            (None, '17, 19', '1'),
        ]
    },
    'depth-first-search': {
        'function': 'dfs',
        'tests': [
            ({'0': ['1', '2'], '1': ['3'], '2': ['4'], '3': [], '4': []}, '"0"', "['0', '1', '3', '2', '4']"),
        ]
    },
    'breadth-first-search': {
        'function': 'bfs',
        'tests': [
            ({'0': ['1', '2'], '1': ['3'], '2': ['4'], '3': [], '4': []}, '"0"', "['0', '1', '2', '3', '4']"),
        ]
    },
    'coin-change': {
        'function': 'coin_change',
        'tests': [
            ('[1, 2, 5]', '11', '3'),
            ('[2]', '3', '-1'),
            ('[1]', '0', '0'),
        ]
    },
    'edit-distance': {
        'function': 'edit_distance',
        'tests': [
            (None, '"kitten", "sitting"', '3'),
            (None, '"horse", "ros"', '3'),
            (None, '"", ""', '0'),
        ]
    },
    'knapsack-problem': {
        'function': 'knapsack_01',
        'tests': [
            ('[10, 20, 30]', '[60, 100, 120], 50', '220'),
            ('[1, 1, 1]', '[10, 20, 30], 2', '50'),
        ]
    },
    'longest-common-subsequence': {
        'function': 'lcs_length',
        'tests': [
            (None, '"ABCDGH", "AEDFHR"', '3'),
            (None, '"AGGTAB", "GXTXAYB"', '4'),
        ]
    },
    'matrix-multiplication': {
        'function': 'matrix_multiply',
        'tests': [
            ('[[1, 2], [3, 4]]', '[[5, 6], [7, 8]]', '[[19, 22], [43, 50]]'),
        ]
    },
    'sieve-of-eratosthenes': {
        'function': 'sieve_of_eratosthenes',
        'tests': [
            (None, '10', '[2, 3, 5, 7]'),
            (None, '20', '[2, 3, 5, 7, 11, 13, 17, 19]'),
            (None, '2', '[]'),
        ]
    },
    'two_pointers': {
        'function': 'two_sum',
        'tests': [
            ('[2, 7, 11, 15]', '9', '[0, 1]'),
            ('[3, 2, 4]', '6', '[1, 2]'),
        ]
    },
    'binary-search-tree': {
        'function': 'BST',
        'tests': [],  # Requires class instantiation
    },
    'linked-list': {
        'function': 'LinkedList',
        'tests': [],  # Requires class instantiation
    },
    'trie': {
        'function': 'Trie',
        'tests': [],  # Requires class instantiation
    },
    'dijkstra-algorithm': {
        'function': 'dijkstra',
        'tests': [],  # Complex graph structure
    },
    'topological-sort': {
        'function': 'topological_sort',
        'tests': [],  # Complex graph structure
    },
    'kmp-algorithm': {
        'function': 'kmp_search',
        'tests': [
            (None, '"ABABDABACDABABCABAB", "ABABCABAB"', '10'),
            (None, '"AABAACAADAABAABA", "AABA"', '0'),
        ]
    },
    'linear-regression': {
        'function': 'linear_regression',
        'tests': [],  # Requires numpy/training
    },
    'logistic-regression': {
        'function': 'logistic_regression',
        'tests': [],  # Requires numpy/training
    },
    'decision-trees': {
        'function': 'DecisionTree',
        'tests': [],  # Requires class/training
    },
    'random-forest': {
        'function': 'RandomForest',
        'tests': [],  # Requires class/training
    },
    'support-vector-machines': {
        'function': 'SVM',
        'tests': [],  # Requires class/training
    },
    'k-means-clustering': {
        'function': 'kmeans',
        'tests': [],  # Requires numpy
    },
    'k-nearest-neighbors': {
        'function': 'knn',
        'tests': [],  # Requires numpy
    },
    'gradient-boosting': {
        'function': 'GradientBoosting',
        'tests': [],  # Requires class/training
    },
    'dynamic-programming': {
        'function': 'fibonacci_dp',
        'tests': [
            (None, '10', '55'),
            (None, '5', '5'),
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
        if arr and arr.startswith('['):
            # Direct array literal
            test_code += f'''    arr = {arr}
    assert {func_name}(arr, {arg}) == {expected}

'''
        elif arr:
            # Array with values
            test_code += f'''    arr = [{arr}]
    assert {func_name}(arr, {arg}) == {expected}

'''
        else:
            # No array, just arguments
            test_code += f'''    assert {func_name}({arg}) == {expected}

'''
    
    return test_code

def snake_to_camel(snake_str):
    """Convert snake_case to camelCase"""
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def generate_javascript_test(algo_name, config):
    """Generate JavaScript Jest test file"""
    func_name = config['function']
    # Convert to camelCase for JavaScript
    js_func_name = snake_to_camel(func_name)
    
    # Try different file naming patterns
    file_variants = [
        f'{algo_name}.js',
        f'{algo_name.replace("-", "_")}.js',
        f'{algo_name.replace("_", "-")}.js',
    ]
    
    test_code = f'''const fs = require('fs');
const path = require('path');

// Try to find the implementation file
const algoDir = path.join(__dirname, '../../{algo_name}');
const possibleFiles = {file_variants};
let code = null;

for (const file of possibleFiles) {{
  try {{
    const filePath = path.join(algoDir, file);
    code = fs.readFileSync(filePath, 'utf8');
    break;
  }} catch (e) {{
    // Try next variant
  }}
}}

if (!code) {{
  throw new Error('Could not find implementation file for {algo_name}');
}}

eval(code);

describe('{algo_name.replace("-", " ").replace("_", " ").title()}', () => {{
'''
    
    for i, test in enumerate(config['tests'], 1):
        arr, arg, expected = test
        
        # Convert Python None to JS null
        if arg == 'None':
            arg = 'null'
        if expected == 'None':
            expected = 'null'
            
        test_code += f'''  test('test case {i}', () => {{
'''
        if arr and isinstance(arr, str) and arr.startswith('['):
            # Direct array literal string like "[1, 2, 3]"
            if arg and arg != 'null':
                test_code += f'''    expect({js_func_name}({arr}, {arg})).toEqual({expected});
'''
            else:
                test_code += f'''    expect({js_func_name}({arr})).toEqual({expected});
'''
        elif arr and isinstance(arr, list):
            # List like ['5, 4, 3, 2, 1'] - convert to proper array
            arr_str = arr[0] if len(arr) == 1 else ', '.join(arr)
            if arg and arg != 'null':
                test_code += f'''    expect({js_func_name}([{arr_str}], {arg})).toEqual({expected});
'''
            else:
                test_code += f'''    expect({js_func_name}([{arr_str}])).toEqual({expected});
'''
        elif arr:
            # String like "5, 4, 3, 2, 1"
            if arg and arg != 'null':
                test_code += f'''    expect({js_func_name}([{arr}], {arg})).toEqual({expected});
'''
            else:
                test_code += f'''    expect({js_func_name}([{arr}])).toEqual({expected});
'''
        else:
            # No array, just arguments
            test_code += f'''    expect({js_func_name}({arg})).toBe({expected});
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
        
        # Skip if no tests defined
        if not config['tests']:
            print(f"⏭️  Skipping {algo_name} (no tests defined - requires manual implementation)")
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
