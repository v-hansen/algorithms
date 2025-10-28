const fs = require('fs');
const path = require('path');

// Load implementation
const algoPath = path.join(__dirname, '../../dynamic-programming/dynamic-programming.js');
const code = fs.readFileSync(algoPath, 'utf8');
eval(code);

describe('Dynamic Programming', () => {
  test('test case 1', () => {
    expect(fibonacci_dp(10)).toBe(55);
  });

  test('test case 2', () => {
    expect(fibonacci_dp(5)).toBe(5);
  });

});
