#!/usr/bin/env python3
import os
import glob

def complete_sorting_algorithms():
    """Completa algoritmos de ordenação"""
    
    # Bubble Sort - completar implementações pequenas
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/bubble-sort"
    
    implementations = {
        "bubble-sort.py": """def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))""",
        
        "bubble-sort.js": """function bubbleSort(arr) {
    const n = arr.length;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
            }
        }
    }
    return arr;
}

console.log(bubbleSort([64, 34, 25, 12, 22, 11, 90]));""",
        
        "bubble-sort.rb": """def bubble_sort(arr)
  n = arr.length
  (0...n).each do |i|
    (0...(n-i-1)).each do |j|
      if arr[j] > arr[j+1]
        arr[j], arr[j+1] = arr[j+1], arr[j]
      end
    end
  end
  arr
end

puts bubble_sort([64, 34, 25, 12, 22, 11, 90]).inspect""",
        
        "bubble-sort.ts": """function bubbleSort(arr: number[]): number[] {
    const n = arr.length;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
            }
        }
    }
    return arr;
}

console.log(bubbleSort([64, 34, 25, 12, 22, 11, 90]));"""
    }
    
    for filename, code in implementations.items():
        with open(f"{base_dir}/{filename}", "w") as f:
            f.write(code)

def complete_search_algorithms():
    """Completa algoritmos de busca"""
    
    # Linear Search - expandir todas as implementações pequenas
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/linear-search"
    
    files_to_expand = [
        ("linear-search.py", """def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

def linear_search_recursive(arr, target, index=0):
    if index >= len(arr):
        return -1
    if arr[index] == target:
        return index
    return linear_search_recursive(arr, target, index + 1)

print(linear_search([1, 2, 3, 4, 5], 3))
print(linear_search_recursive([1, 2, 3, 4, 5], 3))"""),
        
        ("linear-search.js", """function linearSearch(arr, target) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === target) return i;
    }
    return -1;
}

function linearSearchRecursive(arr, target, index = 0) {
    if (index >= arr.length) return -1;
    if (arr[index] === target) return index;
    return linearSearchRecursive(arr, target, index + 1);
}

console.log(linearSearch([1, 2, 3, 4, 5], 3));
console.log(linearSearchRecursive([1, 2, 3, 4, 5], 3));"""),
        
        ("linear-search.ts", """function linearSearch(arr: number[], target: number): number {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === target) return i;
    }
    return -1;
}

function linearSearchRecursive(arr: number[], target: number, index: number = 0): number {
    if (index >= arr.length) return -1;
    if (arr[index] === target) return index;
    return linearSearchRecursive(arr, target, index + 1);
}

console.log(linearSearch([1, 2, 3, 4, 5], 3));
console.log(linearSearchRecursive([1, 2, 3, 4, 5], 3));""")
    ]
    
    for filename, code in files_to_expand:
        with open(f"{base_dir}/{filename}", "w") as f:
            f.write(code)

def complete_two_pointers():
    """Completa algoritmo Two Pointers"""
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/two_pointers"
    
    # Expandir implementações pequenas
    files_to_expand = [
        ("two_pointers.py", """def two_sum(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

print(two_sum([1, 2, 3, 4, 5], 7))
print(is_palindrome("racecar"))"""),
        
        ("two_pointers.js", """function twoSum(arr, target) {
    let left = 0, right = arr.length - 1;
    while (left < right) {
        const sum = arr[left] + arr[right];
        if (sum === target) return [left, right];
        else if (sum < target) left++;
        else right--;
    }
    return [];
}

function isPalindrome(s) {
    let left = 0, right = s.length - 1;
    while (left < right) {
        if (s[left] !== s[right]) return false;
        left++;
        right--;
    }
    return true;
}

console.log(twoSum([1, 2, 3, 4, 5], 7));
console.log(isPalindrome("racecar"));"""),
        
        ("two_pointers.ts", """function twoSum(arr: number[], target: number): number[] {
    let left = 0, right = arr.length - 1;
    while (left < right) {
        const sum = arr[left] + arr[right];
        if (sum === target) return [left, right];
        else if (sum < target) left++;
        else right--;
    }
    return [];
}

function isPalindrome(s: string): boolean {
    let left = 0, right = s.length - 1;
    while (left < right) {
        if (s[left] !== s[right]) return false;
        left++;
        right--;
    }
    return true;
}

console.log(twoSum([1, 2, 3, 4, 5], 7));
console.log(isPalindrome("racecar"));""")
    ]
    
    for filename, code in files_to_expand:
        with open(f"{base_dir}/{filename}", "w") as f:
            f.write(code)

def complete_fibonacci():
    """Completa implementações do Fibonacci"""
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/fibonacci"
    
    # Expandir implementações pequenas
    files_to_expand = [
        ("fibonacci.py", """def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]

print(f"Recursive: {fibonacci_recursive(10)}")
print(f"Iterative: {fibonacci_iterative(10)}")
print(f"Memoized: {fibonacci_memoized(10)}")"""),
        
        ("fibonacci.js", """function fibonacciRecursive(n) {
    if (n <= 1) return n;
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}

function fibonacciIterative(n) {
    if (n <= 1) return n;
    let a = 0, b = 1;
    for (let i = 2; i <= n; i++) {
        [a, b] = [b, a + b];
    }
    return b;
}

const fibonacciMemoized = (function() {
    const memo = {};
    return function(n) {
        if (n in memo) return memo[n];
        if (n <= 1) return n;
        return memo[n] = fibonacciMemoized(n - 1) + fibonacciMemoized(n - 2);
    };
})();

console.log("Recursive:", fibonacciRecursive(10));
console.log("Iterative:", fibonacciIterative(10));
console.log("Memoized:", fibonacciMemoized(10));""")
    ]
    
    for filename, code in files_to_expand:
        with open(f"{base_dir}/{filename}", "w") as f:
            f.write(code)

if __name__ == "__main__":
    print("Completando todas as implementações restantes...")
    complete_sorting_algorithms()
    complete_search_algorithms()
    complete_two_pointers()
    complete_fibonacci()
    print("Algoritmos básicos completados!")
