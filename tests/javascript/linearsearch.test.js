const fs = require('fs');
const path = require('path');

// Load implementation
const algoPath = path.join(__dirname, '../../linear-search/linear-search.js');
const code = fs.readFileSync(algoPath, 'utf8');
eval(code);

describe('Linear Search', () => {
  test('test case 1', () => {
    expect(linear_search([['3, 1, 4, 1, 5']], 4)).toBe(2);
  });

  test('test case 2', () => {
    expect(linear_search([['3, 1, 4, 1, 5']], 9)).toBe(-1);
  });

  test('test case 3', () => {
    expect(linear_search([[]], 1)).toBe(-1);
  });

});
