const fs = require('fs');
const path = require('path');

// Load implementation
const algoPath = path.join(__dirname, '../../longest-common-subsequence/longest-common-subsequence.js');
const code = fs.readFileSync(algoPath, 'utf8');
eval(code);

describe('Longest Common Subsequence', () => {
  test('test case 1', () => {
    expect(lcs("ABCDGH", "AEDFHR")).toBe(3);
  });

  test('test case 2', () => {
    expect(lcs("AGGTAB", "GXTXAYB")).toBe(4);
  });

});
