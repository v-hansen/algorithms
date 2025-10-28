const fs = require('fs');
const path = require('path');

// Load implementation
const algoPath = path.join(__dirname, '../../sieve-of-eratosthenes/sieve-of-eratosthenes.js');
const code = fs.readFileSync(algoPath, 'utf8');
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
