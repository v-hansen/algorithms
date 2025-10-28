const fs = require('fs');
const path = require('path');

// Load the merge sort implementation
const mergeSortPath = path.join(__dirname, '../../merge-sort/merge_sort.js');
const code = fs.readFileSync(mergeSortPath, 'utf8');
eval(code);

describe('Merge Sort', () => {
  test('sorts already sorted array', () => {
    expect(mergeSort([1, 2, 3, 4, 5])).toEqual([1, 2, 3, 4, 5]);
  });

  test('sorts reverse sorted array', () => {
    expect(mergeSort([5, 4, 3, 2, 1])).toEqual([1, 2, 3, 4, 5]);
  });

  test('sorts random order array', () => {
    expect(mergeSort([3, 1, 4, 1, 5, 9, 2, 6])).toEqual([1, 1, 2, 3, 4, 5, 6, 9]);
  });

  test('handles empty array', () => {
    expect(mergeSort([])).toEqual([]);
  });

  test('handles single element', () => {
    expect(mergeSort([42])).toEqual([42]);
  });

  test('handles duplicates', () => {
    expect(mergeSort([3, 3, 1, 1, 2, 2])).toEqual([1, 1, 2, 2, 3, 3]);
  });

  test('handles negative numbers', () => {
    expect(mergeSort([-3, -1, -5, 0, 2])).toEqual([-5, -3, -1, 0, 2]);
  });
});
