const fs = require('fs');
const path = require('path');

const algoDir = path.join(__dirname, '../../dijkstra-algorithm');
const possibleFiles = ['dijkstra_algorithm.js', 'dijkstra.js', 'dijkstra-algorithm.js'];
let code = null;

for (const file of possibleFiles) {
  try {
    code = fs.readFileSync(path.join(algoDir, file), 'utf8');
    break;
  } catch (e) {}
}

if (!code) throw new Error('Could not find implementation file');

const func = new Function(code + '; return dijkstra;');
const dijkstra = func();

describe('Dijkstra Algorithm', () => {
  test('shortest path', () => {
    const graph = {
      'A': {'B': 1, 'C': 4},
      'B': {'C': 2, 'D': 5},
      'C': {'D': 1},
      'D': {}
    };
    const result = dijkstra(graph, 'A');
    expect(result['D']).toBe(4);
  });
});
