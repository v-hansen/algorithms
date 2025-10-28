const fs = require('fs');
const path = require('path');

// Load implementation
const algoPath = path.join(__dirname, '../../matrix-multiplication/matrix-multiplication.js');
const code = fs.readFileSync(algoPath, 'utf8');
eval(code);

describe('Matrix Multiplication', () => {
  test('test case 1', () => {
    expect(matrix_multiply([[[1, 2], [3, 4]]], [[5, 6], [7, 8]])).toBe([[19, 22], [43, 50]]);
  });

});
