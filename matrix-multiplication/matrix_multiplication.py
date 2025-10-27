def matrix_multiply(A, B):
    """Standard matrix multiplication O(n^3)"""
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    
    if cols_A != rows_B:
        raise ValueError("Cannot multiply matrices: incompatible dimensions")
    
    # Initialize result matrix
    C = [[0] * cols_B for _ in range(rows_A)]
    
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    
    return C

def strassen_multiply(A, B):
    """Strassen's algorithm O(n^2.807)"""
    n = len(A)
    
    # Base case
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    
    # Divide matrices into quadrants
    mid = n // 2
    
    A11 = [[A[i][j] for j in range(mid)] for i in range(mid)]
    A12 = [[A[i][j] for j in range(mid, n)] for i in range(mid)]
    A21 = [[A[i][j] for j in range(mid)] for i in range(mid, n)]
    A22 = [[A[i][j] for j in range(mid, n)] for i in range(mid, n)]
    
    B11 = [[B[i][j] for j in range(mid)] for i in range(mid)]
    B12 = [[B[i][j] for j in range(mid, n)] for i in range(mid)]
    B21 = [[B[i][j] for j in range(mid)] for i in range(mid, n)]
    B22 = [[B[i][j] for j in range(mid, n)] for i in range(mid, n)]
    
    # Calculate Strassen's 7 products
    M1 = strassen_multiply(matrix_add(A11, A22), matrix_add(B11, B22))
    M2 = strassen_multiply(matrix_add(A21, A22), B11)
    M3 = strassen_multiply(A11, matrix_subtract(B12, B22))
    M4 = strassen_multiply(A22, matrix_subtract(B21, B11))
    M5 = strassen_multiply(matrix_add(A11, A12), B22)
    M6 = strassen_multiply(matrix_subtract(A21, A11), matrix_add(B11, B12))
    M7 = strassen_multiply(matrix_subtract(A12, A22), matrix_add(B21, B22))
    
    # Calculate result quadrants
    C11 = matrix_subtract(matrix_add(matrix_add(M1, M4), M7), M5)
    C12 = matrix_add(M3, M5)
    C21 = matrix_add(M2, M4)
    C22 = matrix_subtract(matrix_add(matrix_add(M1, M3), M6), M2)
    
    # Combine quadrants
    C = [[0] * n for _ in range(n)]
    for i in range(mid):
        for j in range(mid):
            C[i][j] = C11[i][j]
            C[i][j + mid] = C12[i][j]
            C[i + mid][j] = C21[i][j]
            C[i + mid][j + mid] = C22[i][j]
    
    return C

def matrix_add(A, B):
    """Matrix addition"""
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matrix_subtract(A, B):
    """Matrix subtraction"""
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Test
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = matrix_multiply(A, B)
print("Result:", result)  # [[19, 22], [43, 50]]
