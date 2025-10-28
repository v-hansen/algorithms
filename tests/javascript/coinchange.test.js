const fs = require('fs');
const path = require('path');

// Try to find the implementation file
const algoDir = path.join(__dirname, '../../coin-change');
const possibleFiles = ['coin-change.js', 'coin_change.js', 'coin-change.js'];
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
  throw new Error('Could not find implementation file for coin-change');
}

eval(code);

describe('Coin Change', () => {
  test('test case 1', () => {
    expect(coinChange([1, 2, 5], 11)).toEqual(3);
  });

  test('test case 2', () => {
    expect(coinChange([2], 3)).toEqual(-1);
  });

  test('test case 3', () => {
    expect(coinChange([1], 0)).toEqual(0);
  });

});
