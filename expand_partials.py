#!/usr/bin/env python3
import os
import glob

def expand_all_partials():
    """Expande implementações parciais para completas"""
    
    # Expandir Linear Search - todas as implementações pequenas
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/linear-search"
    
    # Verificar e expandir todos os arquivos pequenos
    for file_path in glob.glob(f"{base_dir}/*"):
        if os.path.isfile(file_path) and os.path.getsize(file_path) < 400:
            filename = os.path.basename(file_path)
            
            if filename.endswith('.c'):
                with open(file_path, "w") as f:
                    f.write("""#include <stdio.h>
int linearSearch(int arr[], int n, int target) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == target) return i;
    }
    return -1;
}

int linearSearchRecursive(int arr[], int n, int target, int index) {
    if (index >= n) return -1;
    if (arr[index] == target) return index;
    return linearSearchRecursive(arr, n, target, index + 1);
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr)/sizeof(arr[0]);
    printf("Iterative: %d\\n", linearSearch(arr, n, 3));
    printf("Recursive: %d\\n", linearSearchRecursive(arr, n, 3, 0));
    return 0;
}""")
            
            elif filename.endswith('.cpp'):
                with open(file_path, "w") as f:
                    f.write("""#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int linearSearch(const vector<int>& arr, int target) {
    auto it = find(arr.begin(), arr.end(), target);
    return it != arr.end() ? distance(arr.begin(), it) : -1;
}

int linearSearchManual(const vector<int>& arr, int target) {
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] == target) return i;
    }
    return -1;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    cout << "STL: " << linearSearch(arr, 3) << endl;
    cout << "Manual: " << linearSearchManual(arr, 3) << endl;
    return 0;
}""")
            
            elif filename.endswith('.rs'):
                with open(file_path, "w") as f:
                    f.write("""fn linear_search(arr: &[i32], target: i32) -> Option<usize> {
    arr.iter().position(|&x| x == target)
}

fn linear_search_manual(arr: &[i32], target: i32) -> Option<usize> {
    for (i, &val) in arr.iter().enumerate() {
        if val == target {
            return Some(i);
        }
    }
    None
}

fn main() {
    let arr = [1, 2, 3, 4, 5];
    println!("Iterator: {:?}", linear_search(&arr, 3));
    println!("Manual: {:?}", linear_search_manual(&arr, 3));
}""")
            
            elif filename.endswith('.kt'):
                with open(file_path, "w") as f:
                    f.write("""fun linearSearch(arr: IntArray, target: Int): Int {
    return arr.indexOf(target)
}

fun linearSearchManual(arr: IntArray, target: Int): Int {
    for (i in arr.indices) {
        if (arr[i] == target) return i
    }
    return -1
}

fun linearSearchRecursive(arr: IntArray, target: Int, index: Int = 0): Int {
    if (index >= arr.size) return -1
    if (arr[index] == target) return index
    return linearSearchRecursive(arr, target, index + 1)
}

fun main() {
    val arr = intArrayOf(1, 2, 3, 4, 5)
    println("Built-in: ${linearSearch(arr, 3)}")
    println("Manual: ${linearSearchManual(arr, 3)}")
    println("Recursive: ${linearSearchRecursive(arr, 3)}")
}""")

    # Expandir Bubble Sort
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/bubble-sort"
    
    for file_path in glob.glob(f"{base_dir}/*"):
        if os.path.isfile(file_path) and os.path.getsize(file_path) < 600:
            filename = os.path.basename(file_path)
            
            if filename.endswith('.rs'):
                with open(file_path, "w") as f:
                    f.write("""fn bubble_sort(arr: &mut [i32]) {
    let n = arr.len();
    for i in 0..n {
        let mut swapped = false;
        for j in 0..n-1-i {
            if arr[j] > arr[j+1] {
                arr.swap(j, j+1);
                swapped = true;
            }
        }
        if !swapped { break; }
    }
}

fn bubble_sort_optimized(arr: &mut [i32]) {
    let mut n = arr.len();
    while n > 1 {
        let mut new_n = 0;
        for i in 1..n {
            if arr[i-1] > arr[i] {
                arr.swap(i-1, i);
                new_n = i;
            }
        }
        n = new_n;
    }
}

fn main() {
    let mut arr1 = [64, 34, 25, 12, 22, 11, 90];
    let mut arr2 = arr1.clone();
    
    bubble_sort(&mut arr1);
    println!("Basic: {:?}", arr1);
    
    bubble_sort_optimized(&mut arr2);
    println!("Optimized: {:?}", arr2);
}""")
            
            elif filename.endswith('.clj'):
                with open(file_path, "w") as f:
                    f.write("""(defn bubble-sort [arr]
  (let [n (count arr)]
    (loop [arr arr i 0]
      (if (>= i (dec n))
        arr
        (let [new-arr (loop [arr arr j 0 swapped false]
                       (if (>= j (- n i 1))
                         (if swapped arr (reduced arr))
                         (if (> (nth arr j) (nth arr (inc j)))
                           (recur (assoc arr j (nth arr (inc j)) (inc j) (nth arr j))
                                  (inc j) true)
                           (recur arr (inc j) swapped))))]
          (if (reduced? new-arr)
            @new-arr
            (recur new-arr (inc i))))))))

(defn bubble-sort-simple [arr]
  (reduce (fn [acc _]
           (reduce (fn [arr i]
                    (if (and (< (inc i) (count arr))
                            (> (nth arr i) (nth arr (inc i))))
                      (assoc arr i (nth arr (inc i)) (inc i) (nth arr i))
                      arr))
                  acc (range (dec (count acc)))))
         arr (range (count arr))))

(println (bubble-sort [64 34 25 12 22 11 90]))
(println (bubble-sort-simple [64 34 25 12 22 11 90]))""")

    # Expandir Palindrome
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/palindrome"
    
    for file_path in glob.glob(f"{base_dir}/*"):
        if os.path.isfile(file_path) and os.path.getsize(file_path) < 500:
            filename = os.path.basename(file_path)
            
            if filename.endswith('.c'):
                with open(file_path, "w") as f:
                    f.write("""#include <stdio.h>
#include <string.h>
#include <ctype.h>

int isPalindrome(char* s) {
    int left = 0, right = strlen(s) - 1;
    while (left < right) {
        if (s[left] != s[right]) return 0;
        left++;
        right--;
    }
    return 1;
}

int isPalindromeIgnoreCase(char* s) {
    int left = 0, right = strlen(s) - 1;
    while (left < right) {
        if (tolower(s[left]) != tolower(s[right])) return 0;
        left++;
        right--;
    }
    return 1;
}

int main() {
    printf("%d\\n", isPalindrome("racecar"));
    printf("%d\\n", isPalindromeIgnoreCase("RaceCar"));
    return 0;
}""")
            
            elif filename.endswith('.go'):
                with open(file_path, "w") as f:
                    f.write("""package main
import (
    "fmt"
    "strings"
    "unicode"
)

func isPalindrome(s string) bool {
    runes := []rune(s)
    left, right := 0, len(runes)-1
    for left < right {
        if runes[left] != runes[right] {
            return false
        }
        left++
        right--
    }
    return true
}

func isPalindromeClean(s string) bool {
    s = strings.ToLower(s)
    var cleaned []rune
    for _, r := range s {
        if unicode.IsLetter(r) || unicode.IsDigit(r) {
            cleaned = append(cleaned, r)
        }
    }
    
    left, right := 0, len(cleaned)-1
    for left < right {
        if cleaned[left] != cleaned[right] {
            return false
        }
        left++
        right--
    }
    return true
}

func main() {
    fmt.Println(isPalindrome("racecar"))
    fmt.Println(isPalindromeClean("A man, a plan, a canal: Panama"))
}""")

if __name__ == "__main__":
    print("Expandindo implementações parciais...")
    expand_all_partials()
    print("Expansão de implementações parciais concluída!")
