const fs = require('fs');
const path = require('path');

// Load implementation
const algoPath = path.join(__dirname, '../../heap-sort/heap-sort.js');
const code = fs.readFileSync(algoPath, 'utf8');
eval(code);

describe('Heap Sort', () => {
  test('test case 1', () => {
    expect(heap_sort([['5, 4, 3, 2, 1']], None)).toBe([1, 2, 3, 4, 5]);
  });

});
