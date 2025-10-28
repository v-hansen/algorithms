const fs = require('fs');
const path = require('path');

// Try to find the implementation file
const algoDir = path.join(__dirname, '../../sieve-of-eratosthenes');
const possibleFiles = ['sieve-of-eratosthenes.js', 'sieve_of_eratosthenes.js', 'sieve-of-eratosthenes.js'];
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
  throw new Error('Could not find implementation file for sieve-of-eratosthenes');
}

eval(code);

describe('Sieve Of Eratosthenes', () => {
  test('test case 1', () => {
    expect(sieve_of_eratosthenes(10)).toBe([2, 3, 5, 7]);
  });

  test('test case 2', () => {
    expect(sieve_of_eratosthenes(20)).toBe([2, 3, 5, 7, 11, 13, 17, 19]);
  });

  test('test case 3', () => {
    expect(sieve_of_eratosthenes(2)).toBe([]);
  });

});
