const fs = require('fs');
const path = require('path');

// Load implementation
const algoPath = path.join(__dirname, '../../euclidean-algorithm/euclidean-algorithm.js');
const code = fs.readFileSync(algoPath, 'utf8');
eval(code);

describe('Euclidean Algorithm', () => {
  test('test case 1', () => {
    expect(gcd(48, 18)).toBe(6);
  });

  test('test case 2', () => {
    expect(gcd(100, 50)).toBe(50);
  });

  test('test case 3', () => {
    expect(gcd(17, 19)).toBe(1);
  });

});
