const fs = require('fs');
const path = require('path');

// Try to find the implementation file
const algoDir = path.join(__dirname, '../../linear-search');
const possibleFiles = ['linear-search.js', 'linear_search.js', 'linear-search.js'];
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
  throw new Error('Could not find implementation file for linear-search');
}

eval(code);

describe('Linear Search', () => {
  test('test case 1', () => {
    expect(linearSearch([3, 1, 4, 1, 5], 4)).toEqual(2);
  });

  test('test case 2', () => {
    expect(linearSearch([3, 1, 4, 1, 5], 9)).toEqual(-1);
  });

  test('test case 3', () => {
    expect(linearSearch([], 1)).toEqual(-1);
  });

});
