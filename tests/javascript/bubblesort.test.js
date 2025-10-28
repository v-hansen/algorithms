const fs = require('fs');
const path = require('path');

// Load implementation
const algoPath = path.join(__dirname, '../../bubble-sort/bubble-sort.js');
const code = fs.readFileSync(algoPath, 'utf8');
eval(code);

describe('Bubble Sort', () => {
  test('test case 1', () => {
    expect(bubble_sort([['5, 4, 3, 2, 1']], None)).toBe([1, 2, 3, 4, 5]);
  });

  test('test case 2', () => {
    expect(bubble_sort([['1, 2, 3']], None)).toBe([1, 2, 3]);
  });

});
