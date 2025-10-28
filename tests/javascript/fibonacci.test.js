const fs = require('fs');
const path = require('path');

// Load implementation
const algoPath = path.join(__dirname, '../../fibonacci/fibonacci.js');
const code = fs.readFileSync(algoPath, 'utf8');
eval(code);

describe('Fibonacci', () => {
  test('test case 1', () => {
    expect(fibonacci(0)).toBe(0);
  });

  test('test case 2', () => {
    expect(fibonacci(1)).toBe(1);
  });

  test('test case 3', () => {
    expect(fibonacci(5)).toBe(5);
  });

  test('test case 4', () => {
    expect(fibonacci(10)).toBe(55);
  });

});
