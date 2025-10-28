const fs = require('fs');
const path = require('path');

// Try to find the implementation file
const algoDir = path.join(__dirname, '../../longest-common-subsequence');
const possibleFiles = ['longest-common-subsequence.js', 'longest_common_subsequence.js', 'longest-common-subsequence.js'];
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
  throw new Error('Could not find implementation file for longest-common-subsequence');
}

eval(code);

describe('Longest Common Subsequence', () => {
  test('test case 1', () => {
    expect(lcsLength("ABCDGH", "AEDFHR")).toBe(3);
  });

  test('test case 2', () => {
    expect(lcsLength("AGGTAB", "GXTXAYB")).toBe(4);
  });

});
