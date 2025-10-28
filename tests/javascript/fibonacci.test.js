const fs = require('fs');
const path = require('path');

// Try to find the implementation file
const algoDir = path.join(__dirname, '../../fibonacci');
const possibleFiles = ['fibonacci.js', 'fibonacci.js', 'fibonacci.js'];
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
  throw new Error('Could not find implementation file for fibonacci');
}

eval(code);

describe('Fibonacci', () => {
  test('test case 1', () => {
    expect(fibonacci_iterative(0)).toBe(0);
  });

  test('test case 2', () => {
    expect(fibonacci_iterative(1)).toBe(1);
  });

  test('test case 3', () => {
    expect(fibonacci_iterative(5)).toBe(5);
  });

  test('test case 4', () => {
    expect(fibonacci_iterative(10)).toBe(55);
  });

});
