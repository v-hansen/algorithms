const fs = require('fs');
const path = require('path');

// Load implementation
const algoPath = path.join(__dirname, '../../kmp-algorithm/kmp-algorithm.js');
const code = fs.readFileSync(algoPath, 'utf8');
eval(code);

describe('Kmp Algorithm', () => {
  test('test case 1', () => {
    expect(kmp_search("ABABDABACDABABCABAB", "ABABCABAB")).toBe(10);
  });

  test('test case 2', () => {
    expect(kmp_search("AABAACAADAABAABA", "AABA")).toBe(0);
  });

});
