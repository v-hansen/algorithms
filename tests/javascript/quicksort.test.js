const fs = require('fs');
const path = require('path');

// Try to find the implementation file
const algoDir = path.join(__dirname, '../../quick-sort');
const possibleFiles = ['quick-sort.js', 'quick_sort.js', 'quick-sort.js'];
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
  throw new Error('Could not find implementation file for quick-sort');
}

eval(code);

describe('Quick Sort', () => {
  test('test case 1', () => {
    expect(quick_sort([['5, 4, 3, 2, 1']], None)).toBe([1, 2, 3, 4, 5]);
  });

  test('test case 2', () => {
    expect(quick_sort([['3, 1, 4, 1, 5']], None)).toBe([1, 1, 3, 4, 5]);
  });

});
