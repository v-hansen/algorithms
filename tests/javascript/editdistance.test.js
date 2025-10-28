const fs = require('fs');
const path = require('path');

// Load implementation
const algoPath = path.join(__dirname, '../../edit-distance/edit-distance.js');
const code = fs.readFileSync(algoPath, 'utf8');
eval(code);

describe('Edit Distance', () => {
  test('test case 1', () => {
    expect(edit_distance("kitten", "sitting")).toBe(3);
  });

  test('test case 2', () => {
    expect(edit_distance("horse", "ros")).toBe(3);
  });

  test('test case 3', () => {
    expect(edit_distance("", "")).toBe(0);
  });

});
