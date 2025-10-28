const fs = require('fs');
const path = require('path');

// Try to find the implementation file
const algoDir = path.join(__dirname, '../../palindrome');
const possibleFiles = ['palindrome.js', 'palindrome.js', 'palindrome.js'];
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
  throw new Error('Could not find implementation file for palindrome');
}

eval(code);

describe('Palindrome', () => {
  test('test case 1', () => {
    expect(isPalindromeSimple("racecar")).toBe(true);
  });

  test('test case 2', () => {
    expect(isPalindromeSimple("hello")).toBe(false);
  });

  test('test case 3', () => {
    expect(isPalindromeSimple("")).toBe(true);
  });

});
