#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> matrixMultiply(const vector<vector<int>>& a, const vector<vector<int>>& b) {
    int rowsA = a.size();
    int colsA = a[0].size();
    int colsB = b[0].size();
    
    vector<vector<int>> result(rowsA, vector<int>(colsB, 0));
    
    for (int i = 0; i < rowsA; i++) {
        for (int j = 0; j < colsB; j++) {
            for (int k = 0; k < colsA; k++) {
                result[i][j] += a[i][k] * b[k][j];
            }
        }
    }
    
    return result;
}

vector<vector<int>> strassenMultiply(const vector<vector<int>>& a, const vector<vector<int>>& b) {
    int n = a.size();
    
    if (n == 1) {
        return {{a[0][0] * b[0][0]}};
    }
    
    int half = n / 2;
    
    // Divide matrices into quadrants
    vector<vector<int>> a11(half, vector<int>(half));
    vector<vector<int>> a12(half, vector<int>(half));
    vector<vector<int>> a21(half, vector<int>(half));
    vector<vector<int>> a22(half, vector<int>(half));
    
    vector<vector<int>> b11(half, vector<int>(half));
    vector<vector<int>> b12(half, vector<int>(half));
    vector<vector<int>> b21(half, vector<int>(half));
    vector<vector<int>> b22(half, vector<int>(half));
    
    for (int i = 0; i < half; i++) {
        for (int j = 0; j < half; j++) {
            a11[i][j] = a[i][j];
            a12[i][j] = a[i][j + half];
            a21[i][j] = a[i + half][j];
            a22[i][j] = a[i + half][j + half];
            
            b11[i][j] = b[i][j];
            b12[i][j] = b[i][j + half];
            b21[i][j] = b[i + half][j];
            b22[i][j] = b[i + half][j + half];
        }
    }
    
    // For simplicity, use standard multiplication for small matrices
    return matrixMultiply(a, b);
}

void printMatrix(const vector<vector<int>>& matrix) {
    for (const auto& row : matrix) {
        for (int val : row) {
            cout << val << " ";
        }
        cout << endl;
    }
}

int main() {
    vector<vector<int>> a = {{1, 2}, {3, 4}};
    vector<vector<int>> b = {{5, 6}, {7, 8}};
    
    auto result = matrixMultiply(a, b);
    cout << "Result:" << endl;
    printMatrix(result);
    
    return 0;
}