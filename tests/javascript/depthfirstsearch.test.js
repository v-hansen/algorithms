const fs = require('fs');
const path = require('path');

// Load implementation
const algoPath = path.join(__dirname, '../../depth-first-search/depth-first-search.js');
const code = fs.readFileSync(algoPath, 'utf8');
eval(code);

describe('Depth First Search', () => {
  test('test case 1', () => {
    expect(dfs([{'0': ['1', '2'], '1': ['3'], '2': ['4'], '3': [], '4': []}], "0")).toBe(['0', '1', '3', '2', '4']);
  });

});
