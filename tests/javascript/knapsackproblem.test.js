const fs = require('fs');
const path = require('path');

// Try to find the implementation file
const algoDir = path.join(__dirname, '../../knapsack-problem');
const possibleFiles = ['knapsack-problem.js', 'knapsack_problem.js', 'knapsack-problem.js'];
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
  throw new Error('Could not find implementation file for knapsack-problem');
}

eval(code);

describe('Knapsack Problem', () => {
  test('test case 1', () => {
    expect(knapsack_01([10, 20, 30], [60, 100, 120], 50)).toEqual(220);
  });

  test('test case 2', () => {
    expect(knapsack_01([1, 1, 1], [10, 20, 30], 2)).toEqual(50);
  });

});
