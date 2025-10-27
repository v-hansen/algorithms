package main

import "fmt"

func computeLPS(pattern string) []int {
    m := len(pattern)
    lps := make([]int, m)
    length := 0
    i := 1
    
    for i < m {
        if pattern[i] == pattern[length] {
            length++
            lps[i] = length
            i++
        } else {
            if length != 0 {
                length = lps[length-1]
            } else {
                lps[i] = 0
                i++
            }
        }
    }
    return lps
}

func kmpSearch(text, pattern string) []int {
    n := len(text)
    m := len(pattern)
    
    if m == 0 {
        return []int{}
    }
    
    lps := computeLPS(pattern)
    var matches []int
    
    i, j := 0, 0
    for i < n {
        if pattern[j] == text[i] {
            i++
            j++
        }
        
        if j == m {
            matches = append(matches, i-j)
            j = lps[j-1]
        } else if i < n && pattern[j] != text[i] {
            if j != 0 {
                j = lps[j-1]
            } else {
                i++
            }
        }
    }
    
    return matches
}

func main() {
    text := "ABABDABACDABABCABCABCABCABC"
    pattern := "ABABCABCABCABC"
    matches := kmpSearch(text, pattern)
    fmt.Printf("Pattern found at indices: %v\n", matches)
}
