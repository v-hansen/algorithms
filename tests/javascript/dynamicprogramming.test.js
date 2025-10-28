const fs = require('fs');
const path = require('path');

// Try to find the implementation file
const algoDir = path.join(__dirname, '../../dynamic-programming');
const possibleFiles = ['dynamic-programming.js', 'dynamic_programming.js', 'dynamic-programming.js'];
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
  throw new Error('Could not find implementation file for dynamic-programming');
}

eval(code);

describe('Dynamic Programming', () => {
  test('test case 1', () => {
    expect(fibMemo(10)).toBe(55);
  });

  test('test case 2', () => {
    expect(fibMemo(5)).toBe(5);
  });

});
