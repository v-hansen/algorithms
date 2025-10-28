const fs = require('fs');
const path = require('path');

// Try to find the implementation file
const algoDir = path.join(__dirname, '../../two_pointers');
const possibleFiles = ['two_pointers.js', 'two_pointers.js', 'two-pointers.js'];
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
  throw new Error('Could not find implementation file for two_pointers');
}

eval(code);

describe('Two Pointers', () => {
  test('test case 1', () => {
    expect(twoSum([2, 7, 11, 15], 9)).toEqual([0, 1]);
  });

  test('test case 2', () => {
    expect(twoSum([2, 3, 4], 6)).toEqual([0, 2]);
  });

});
