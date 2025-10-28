const fs = require('fs');
const path = require('path');

// Try to find the implementation file
const algoDir = path.join(__dirname, '../../euclidean-algorithm');
const possibleFiles = ['euclidean-algorithm.js', 'euclidean_algorithm.js', 'euclidean-algorithm.js'];
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
  throw new Error('Could not find implementation file for euclidean-algorithm');
}

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
