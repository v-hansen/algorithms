package main

import "fmt"

func twoSum(arr []int, target int) []int {
    left, right := 0, len(arr)-1
    for left < right {
        sum := arr[left] + arr[right]
        if sum == target {
            return []int{left, right}
        }
        if sum < target {
            left++
        } else {
            right--
        }
    }
    return []int{}
}

func main() {
    result := twoSum([]int{1, 2, 3, 4, 6}, 6)
    fmt.Printf("[%d, %d]\n", result[0], result[1])
}
