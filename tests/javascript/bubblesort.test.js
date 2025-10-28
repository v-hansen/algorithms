const fs = require('fs');
const path = require('path');

// Try to find the implementation file
const algoDir = path.join(__dirname, '../../bubble-sort');
const possibleFiles = ['bubble-sort.js', 'bubble_sort.js', 'bubble-sort.js'];
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
  throw new Error('Could not find implementation file for bubble-sort');
}

eval(code);

describe('Bubble Sort', () => {
  test('test case 1', () => {
    expect(bubble_sort([['5, 4, 3, 2, 1']], None)).toBe([1, 2, 3, 4, 5]);
  });

  test('test case 2', () => {
    expect(bubble_sort([['1, 2, 3']], None)).toBe([1, 2, 3]);
  });

});
