const fs = require('fs');
const path = require('path');

// Load implementation
const algoPath = path.join(__dirname, '../../quick-sort/quick-sort.js');
const code = fs.readFileSync(algoPath, 'utf8');
eval(code);

describe('Quick Sort', () => {
  test('test case 1', () => {
    expect(quick_sort([['5, 4, 3, 2, 1']], None)).toBe([1, 2, 3, 4, 5]);
  });

  test('test case 2', () => {
    expect(quick_sort([['3, 1, 4, 1, 5']], None)).toBe([1, 1, 3, 4, 5]);
  });

});
