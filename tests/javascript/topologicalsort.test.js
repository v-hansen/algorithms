const fs = require('fs');
const path = require('path');

const algoDir = path.join(__dirname, '../../topological-sort');
const possibleFiles = ['topological_sort.js', 'topological-sort.js', 'topologicalSort.js'];
let code = null;

for (const file of possibleFiles) {
  try {
    code = fs.readFileSync(path.join(algoDir, file), 'utf8');
    break;
  } catch (e) {}
}

if (!code) throw new Error('Could not find implementation file');

// Remove test code that runs automatically
const originalLog = console.log;
console.log = () => {};

const func = new Function(code + '; return topologicalSortDFS || topologicalSort;');
console.log = originalLog;
const topologicalSort = func();

describe('Topological Sort', () => {
  test('basic graph', () => {
    const graph = {5: [2, 0], 4: [0, 1], 2: [3], 3: [1], 0: [], 1: []};
    const result = topologicalSort(graph, 6);
    expect(Array.isArray(result)).toBe(true);
    expect(result.length).toBe(6);
  });
});
