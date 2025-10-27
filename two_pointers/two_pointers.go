package main
import "fmt"

func twoSum(arr []int, target int) []int {
    left, right := 0, len(arr)-1
    for left < right {
        sum := arr[left] + arr[right]
        if sum == target {
            return []int{left, right}
        } else if sum < target {
            left++
        } else {
            right--
        }
    }
    return []int{}
}

func main() {
    arr := []int{1, 2, 3, 4, 5}
    result := twoSum(arr, 7)
    fmt.Println(result)
}