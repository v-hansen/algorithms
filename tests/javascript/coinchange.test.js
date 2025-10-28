const fs = require('fs');
const path = require('path');

// Load implementation
const algoPath = path.join(__dirname, '../../coin-change/coin-change.js');
const code = fs.readFileSync(algoPath, 'utf8');
eval(code);

describe('Coin Change', () => {
  test('test case 1', () => {
    expect(coin_change([[1, 2, 5]], 11)).toBe(3);
  });

  test('test case 2', () => {
    expect(coin_change([[2]], 3)).toBe(-1);
  });

  test('test case 3', () => {
    expect(coin_change([[1]], 0)).toBe(0);
  });

});
