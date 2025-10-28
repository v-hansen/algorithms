const fs = require('fs');
const path = require('path');

// Try to find the implementation file
const algoDir = path.join(__dirname, '../../kmp-algorithm');
const possibleFiles = ['kmp-algorithm.js', 'kmp_algorithm.js', 'kmp-algorithm.js'];
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
  throw new Error('Could not find implementation file for kmp-algorithm');
}

eval(code);

describe('Kmp Algorithm', () => {
  test('test case 1', () => {
    expect(kmpSearch("ABABDABACDABABCABAB", "ABABCABAB")).toBe(10);
  });

  test('test case 2', () => {
    expect(kmpSearch("AABAACAADAABAABA", "AABA")).toBe(0);
  });

});
