package main
import "fmt"

func matrixMultiply(a, b [][]int) [][]int {
    rowsA, colsA := len(a), len(a[0])
    colsB := len(b[0])
    
    result := make([][]int, rowsA)
    for i := range result {
        result[i] = make([]int, colsB)
    }
    
    for i := 0; i < rowsA; i++ {
        for j := 0; j < colsB; j++ {
            for k := 0; k < colsA; k++ {
                result[i][j] += a[i][k] * b[k][j]
            }
        }
    }
    
    return result
}

func addMatrices(a, b [][]int) [][]int {
    rows, cols := len(a), len(a[0])
    result := make([][]int, rows)
    for i := range result {
        result[i] = make([]int, cols)
        for j := range result[i] {
            result[i][j] = a[i][j] + b[i][j]
        }
    }
    return result
}

func subtractMatrices(a, b [][]int) [][]int {
    rows, cols := len(a), len(a[0])
    result := make([][]int, rows)
    for i := range result {
        result[i] = make([]int, cols)
        for j := range result[i] {
            result[i][j] = a[i][j] - b[i][j]
        }
    }
    return result
}

func printMatrix(matrix [][]int) {
    for _, row := range matrix {
        for _, val := range row {
            fmt.Printf("%d ", val)
        }
        fmt.Println()
    }
}

func main() {
    a := [][]int{{1, 2}, {3, 4}}
    b := [][]int{{5, 6}, {7, 8}}
    
    result := matrixMultiply(a, b)
    fmt.Println("Result:")
    printMatrix(result)
}