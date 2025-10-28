const fs = require('fs');
const path = require('path');

// Try to find the implementation file
const algoDir = path.join(__dirname, '../../merge-sort');
const possibleFiles = ['merge-sort.js', 'merge_sort.js', 'merge-sort.js'];
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
  throw new Error('Could not find implementation file for merge-sort');
}

eval(code);

describe('Merge Sort', () => {
  test('test case 1', () => {
    expect(merge_sort([['5, 4, 3, 2, 1']], None)).toBe([1, 2, 3, 4, 5]);
  });

  test('test case 2', () => {
    expect(merge_sort([['1, 2, 3, 4, 5']], None)).toBe([1, 2, 3, 4, 5]);
  });

  test('test case 3', () => {
    expect(merge_sort([], None)).toEqual([]);
  });

});
