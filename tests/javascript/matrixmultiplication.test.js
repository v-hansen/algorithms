const fs = require('fs');
const path = require('path');

// Try to find the implementation file
const algoDir = path.join(__dirname, '../../matrix-multiplication');
const possibleFiles = ['matrix-multiplication.js', 'matrix_multiplication.js', 'matrix-multiplication.js'];
let code = null;

for (const file of possibleFiles) {
  try {
    const filePath = path.join(algoDir, file);
    code = fs.readFileSync(filePath, 'utf8');
    break;
  } catch (e) {
    // Try next variant
  }
}

if (!code) {
  throw new Error('Could not find implementation file for matrix-multiplication');
}

eval(code);

describe('Matrix Multiplication', () => {
  test('test case 1', () => {
    expect(matrixMultiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])).toEqual([[19, 22], [43, 50]]);
  });

});
