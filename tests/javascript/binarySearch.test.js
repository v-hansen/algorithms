const fs = require('fs');
const path = require('path');

// Load the binary search implementation
const binarySearchPath = path.join(__dirname, '../../binary-search/binary-search.js');
const code = fs.readFileSync(binarySearchPath, 'utf8');
eval(code);

describe('Binary Search', () => {
  test('finds element in middle', () => {
    expect(binarySearch([1, 2, 3, 4, 5], 3)).toBe(2);
  });

  test('finds first element', () => {
    expect(binarySearch([1, 2, 3, 4, 5], 1)).toBe(0);
  });

  test('finds last element', () => {
    expect(binarySearch([1, 2, 3, 4, 5], 5)).toBe(4);
  });

  test('returns -1 when not found', () => {
    expect(binarySearch([1, 2, 3, 4, 5], 6)).toBe(-1);
  });

  test('handles empty array', () => {
    expect(binarySearch([], 1)).toBe(-1);
  });

  test('handles single element found', () => {
    expect(binarySearch([5], 5)).toBe(0);
  });

  test('handles single element not found', () => {
    expect(binarySearch([5], 3)).toBe(-1);
  });
});
