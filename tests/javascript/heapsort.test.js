const fs = require('fs');
const path = require('path');

// Try to find the implementation file
const algoDir = path.join(__dirname, '../../heap-sort');
const possibleFiles = ['heap-sort.js', 'heap_sort.js', 'heap-sort.js'];
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
  throw new Error('Could not find implementation file for heap-sort');
}

eval(code);

describe('Heap Sort', () => {
  test('test case 1', () => {
    expect(heap_sort([['5, 4, 3, 2, 1']], None)).toBe([1, 2, 3, 4, 5]);
  });

});
