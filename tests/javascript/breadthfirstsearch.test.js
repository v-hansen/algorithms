const fs = require('fs');
const path = require('path');

// Try to find the implementation file
const algoDir = path.join(__dirname, '../../breadth-first-search');
const possibleFiles = ['breadth-first-search.js', 'breadth_first_search.js', 'breadth-first-search.js'];
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
  throw new Error('Could not find implementation file for breadth-first-search');
}

eval(code);

describe('Breadth First Search', () => {
  test('test case 1', () => {
    expect(bfs([{'0': ['1', '2'], '1': ['3'], '2': ['4'], '3': [], '4': []}], "0")).toEqual(['0', '1', '2', '3', '4']);
  });

});
