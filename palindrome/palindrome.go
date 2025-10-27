package main

import (
    "fmt"
    "strings"
)

func isPalindrome(str string) bool {
    str = strings.ToLower(str)
    left, right := 0, len(str)-1
    for left < right {
        if str[left] != str[right] {
            return false
        }
        left++
        right--
    }
    return true
}

func main() {
    fmt.Println(isPalindrome("racecar"))
    fmt.Println(isPalindrome("hello"))
}
