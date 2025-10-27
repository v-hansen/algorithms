package main
import "fmt"

func max(a, b int) int {
    if a > b { return a }
    return b
}

func lcs(X, Y string) int {
    m, n := len(X), len(Y)
    L := make([][]int, m+1)
    for i := range L {
        L[i] = make([]int, n+1)
    }
    
    for i := 0; i <= m; i++ {
        for j := 0; j <= n; j++ {
            if i == 0 || j == 0 {
                L[i][j] = 0
            } else if X[i-1] == Y[j-1] {
                L[i][j] = L[i-1][j-1] + 1
            } else {
                L[i][j] = max(L[i-1][j], L[i][j-1])
            }
        }
    }
    
    return L[m][n]
}

func main() {
    fmt.Println(lcs("ABCDGH", "AEDFHR"))
}