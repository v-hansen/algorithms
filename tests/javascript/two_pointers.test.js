const fs = require('fs');
const path = require('path');

// Load implementation
const algoPath = path.join(__dirname, '../../two_pointers/two-pointers.js');
const code = fs.readFileSync(algoPath, 'utf8');
eval(code);

describe('Two_Pointers', () => {
  test('test case 1', () => {
    expect(two_sum([[2, 7, 11, 15]], 9)).toBe([0, 1]);
  });

  test('test case 2', () => {
    expect(two_sum([[3, 2, 4]], 6)).toBe([1, 2]);
  });

});
