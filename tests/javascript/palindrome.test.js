const fs = require('fs');
const path = require('path');

// Load implementation
const algoPath = path.join(__dirname, '../../palindrome/palindrome.js');
const code = fs.readFileSync(algoPath, 'utf8');
eval(code);

describe('Palindrome', () => {
  test('test case 1', () => {
    expect(is_palindrome("racecar")).toBe(true);
  });

  test('test case 2', () => {
    expect(is_palindrome("hello")).toBe(false);
  });

  test('test case 3', () => {
    expect(is_palindrome("")).toBe(true);
  });

});
