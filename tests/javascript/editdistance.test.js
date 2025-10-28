const fs = require('fs');
const path = require('path');

// Try to find the implementation file
const algoDir = path.join(__dirname, '../../edit-distance');
const possibleFiles = ['edit-distance.js', 'edit_distance.js', 'edit-distance.js'];
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
  throw new Error('Could not find implementation file for edit-distance');
}

eval(code);

describe('Edit Distance', () => {
  test('test case 1', () => {
    expect(editDistance("kitten", "sitting")).toBe(3);
  });

  test('test case 2', () => {
    expect(editDistance("horse", "ros")).toBe(3);
  });

  test('test case 3', () => {
    expect(editDistance("", "")).toBe(0);
  });

});
