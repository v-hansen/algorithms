function matrixMultiply(A, B) {
    const rowsA = A.length;
    const colsA = A[0].length;
    const rowsB = B.length;
    const colsB = B[0].length;
    
    if (colsA !== rowsB) {
        throw new Error("Cannot multiply matrices: incompatible dimensions");
    }
    
    const C = Array(rowsA).fill(null).map(() => Array(colsB).fill(0));
    
    for (let i = 0; i < rowsA; i++) {
        for (let j = 0; j < colsB; j++) {
            for (let k = 0; k < colsA; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
    
    return C;
}

function matrixAdd(A, B) {
    return A.map((row, i) => row.map((val, j) => val + B[i][j]));
}

function matrixSubtract(A, B) {
    return A.map((row, i) => row.map((val, j) => val - B[i][j]));
}

function strassenMultiply(A, B) {
    const n = A.length;
    
    if (n === 1) {
        return [[A[0][0] * B[0][0]]];
    }
    
    const mid = Math.floor(n / 2);
    
    // Divide matrices into quadrants
    const A11 = A.slice(0, mid).map(row => row.slice(0, mid));
    const A12 = A.slice(0, mid).map(row => row.slice(mid));
    const A21 = A.slice(mid).map(row => row.slice(0, mid));
    const A22 = A.slice(mid).map(row => row.slice(mid));
    
    const B11 = B.slice(0, mid).map(row => row.slice(0, mid));
    const B12 = B.slice(0, mid).map(row => row.slice(mid));
    const B21 = B.slice(mid).map(row => row.slice(0, mid));
    const B22 = B.slice(mid).map(row => row.slice(mid));
    
    // Calculate Strassen's 7 products
    const M1 = strassenMultiply(matrixAdd(A11, A22), matrixAdd(B11, B22));
    const M2 = strassenMultiply(matrixAdd(A21, A22), B11);
    const M3 = strassenMultiply(A11, matrixSubtract(B12, B22));
    const M4 = strassenMultiply(A22, matrixSubtract(B21, B11));
    const M5 = strassenMultiply(matrixAdd(A11, A12), B22);
    const M6 = strassenMultiply(matrixSubtract(A21, A11), matrixAdd(B11, B12));
    const M7 = strassenMultiply(matrixSubtract(A12, A22), matrixAdd(B21, B22));
    
    // Calculate result quadrants
    const C11 = matrixSubtract(matrixAdd(matrixAdd(M1, M4), M7), M5);
    const C12 = matrixAdd(M3, M5);
    const C21 = matrixAdd(M2, M4);
    const C22 = matrixSubtract(matrixAdd(matrixAdd(M1, M3), M6), M2);
    
    // Combine quadrants
    const C = Array(n).fill(null).map(() => Array(n).fill(0));
    for (let i = 0; i < mid; i++) {
        for (let j = 0; j < mid; j++) {
            C[i][j] = C11[i][j];
            C[i][j + mid] = C12[i][j];
            C[i + mid][j] = C21[i][j];
            C[i + mid][j + mid] = C22[i][j];
        }
    }
    
    return C;
}

// Test
const A = [[1, 2], [3, 4]];
const B = [[5, 6], [7, 8]];
const result = matrixMultiply(A, B);
console.log("Result:", result); // [[19, 22], [43, 50]]
