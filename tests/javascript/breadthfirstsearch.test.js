const fs = require('fs');
const path = require('path');

// Load implementation
const algoPath = path.join(__dirname, '../../breadth-first-search/breadth-first-search.js');
const code = fs.readFileSync(algoPath, 'utf8');
eval(code);

describe('Breadth First Search', () => {
  test('test case 1', () => {
    expect(bfs([{'0': ['1', '2'], '1': ['3'], '2': ['4'], '3': [], '4': []}], "0")).toBe(['0', '1', '2', '3', '4']);
  });

});
