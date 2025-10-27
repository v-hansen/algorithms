package main

import "fmt"

func linearSearch(arr []int, target int) int {
    for i, val := range arr {
        if val == target {
            return i
        }
    }
    return -1
}

func main() {
    arr := []int{5, 2, 8, 1, 9, 3}
    fmt.Println(linearSearch(arr, 8))
    fmt.Println(linearSearch(arr, 7))
}
