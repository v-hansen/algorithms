package main
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
}