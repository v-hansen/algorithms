function matrixMultiply(a: number[][], b: number[][]): number[][] | null {
    const rowsA = a.length, colsA = a[0].length;
    const rowsB = b.length, colsB = b[0].length;
    
    if (colsA !== rowsB) return null;
    
    const result: number[][] = Array(rowsA).fill(0).map(() => Array(colsB).fill(0));
    
    for (let i = 0; i < rowsA; i++) {
        for (let j = 0; j < colsB; j++) {
            for (let k = 0; k < colsA; k++) {
                result[i][j] += a[i][k] * b[k][j];
            }
        }
    }
    
    return result;
}

const a = [[1, 2], [3, 4]];
const b = [[5, 6], [7, 8]];
console.log(matrixMultiply(a, b));