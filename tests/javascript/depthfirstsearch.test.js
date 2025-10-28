const fs = require('fs');
const path = require('path');

// Try to find the implementation file
const algoDir = path.join(__dirname, '../../depth-first-search');
const possibleFiles = ['depth-first-search.js', 'depth_first_search.js', 'depth-first-search.js'];
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
  throw new Error('Could not find implementation file for depth-first-search');
}

eval(code);

describe('Depth First Search', () => {
  test('test case 1', () => {
    expect(dfs([{'0': ['1', '2'], '1': ['3'], '2': ['4'], '3': [], '4': []}], "0")).toBe(['0', '1', '3', '2', '4']);
  });

});
