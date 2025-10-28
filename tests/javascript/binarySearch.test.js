const fs = require('fs');
const path = require('path');

// Try to find the implementation file
const algoDir = path.join(__dirname, '../../binary-search');
const possibleFiles = ['binary-search.js', 'binary_search.js', 'binary-search.js'];
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
  throw new Error('Could not find implementation file for binary-search');
}

eval(code);

describe('Binary Search', () => {
  test('test case 1', () => {
    expect(binarySearch([1, 2, 3, 4, 5], 3)).toEqual(2);
  });

  test('test case 2', () => {
    expect(binarySearch([1, 2, 3, 4, 5], 1)).toEqual(0);
  });

  test('test case 3', () => {
    expect(binarySearch([1, 2, 3, 4, 5], 6)).toEqual(-1);
  });

  test('test case 4', () => {
    expect(binarySearch([], 1)).toEqual(-1);
  });

});
