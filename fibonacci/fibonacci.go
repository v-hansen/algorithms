package main
import "fmt"

func fibRecursive(n int) int {
    if n <= 1 {
        return n
    }
    return fibRecursive(n-1) + fibRecursive(n-2)
}

func fibIterative(n int) int {
    if n <= 1 {
        return n
    }
    a, b := 0, 1
    for i := 2; i <= n; i++ {
        a, b = b, a+b
    }
    return b
}

func fibMemoized(n int, memo map[int]int) int {
    if n <= 1 {
        return n
    }
    if val, exists := memo[n]; exists {
        return val
    }
    memo[n] = fibMemoized(n-1, memo) + fibMemoized(n-2, memo)
    return memo[n]
}

func main() {
    fmt.Printf("Recursive: %d\n", fibRecursive(10))
    fmt.Printf("Iterative: %d\n", fibIterative(10))
    
    memo := make(map[int]int)
    fmt.Printf("Memoized: %d\n", fibMemoized(10, memo))
}