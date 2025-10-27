#include <stdio.h>
#include <stdlib.h>

void matrixMultiply(int **a, int **b, int **result, int rowsA, int colsA, int colsB) {
    for (int i = 0; i < rowsA; i++) {
        for (int j = 0; j < colsB; j++) {
            result[i][j] = 0;
            for (int k = 0; k < colsA; k++) {
                result[i][j] += a[i][k] * b[k][j];
            }
        }
    }
}

void printMatrix(int **matrix, int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int rowsA = 2, colsA = 2, colsB = 2;
    
    int **a = malloc(rowsA * sizeof(int*));
    int **b = malloc(colsA * sizeof(int*));
    int **result = malloc(rowsA * sizeof(int*));
    
    for (int i = 0; i < rowsA; i++) {
        a[i] = malloc(colsA * sizeof(int));
        result[i] = malloc(colsB * sizeof(int));
    }
    for (int i = 0; i < colsA; i++) {
        b[i] = malloc(colsB * sizeof(int));
    }
    
    // Initialize matrices
    a[0][0] = 1; a[0][1] = 2;
    a[1][0] = 3; a[1][1] = 4;
    
    b[0][0] = 5; b[0][1] = 6;
    b[1][0] = 7; b[1][1] = 8;
    
    matrixMultiply(a, b, result, rowsA, colsA, colsB);
    printMatrix(result, rowsA, colsB);
    
    // Free memory
    for (int i = 0; i < rowsA; i++) {
        free(a[i]);
        free(result[i]);
    }
    for (int i = 0; i < colsA; i++) {
        free(b[i]);
    }
    free(a); free(b); free(result);
    
    return 0;
}