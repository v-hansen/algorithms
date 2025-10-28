const fs = require('fs');
const path = require('path');

// Load implementation
const algoPath = path.join(__dirname, '../../knapsack-problem/knapsack-problem.js');
const code = fs.readFileSync(algoPath, 'utf8');
eval(code);

describe('Knapsack Problem', () => {
  test('test case 1', () => {
    expect(knapsack([[60, 100, 120]], [10, 20, 30], 50)).toBe(220);
  });

  test('test case 2', () => {
    expect(knapsack([[10, 20, 30]], [1, 1, 1], 2)).toBe(50);
  });

});
