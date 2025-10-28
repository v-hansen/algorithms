const fs = require('fs');
const path = require('path');

const algoDir = path.join(__dirname, '../../k-nearest-neighbors');
const possibleFiles = ['knn.js', 'k_nearest_neighbors.js', 'k-nearest-neighbors.js'];
let code = null;

for (const file of possibleFiles) {
  try {
    code = fs.readFileSync(path.join(algoDir, file), 'utf8');
    break;
  } catch (e) {}
}

if (!code) throw new Error('Could not find implementation file');

const originalLog = console.log;
console.log = () => {};
const func = new Function(code + '; return KNN;');
console.log = originalLog;
const KNN = func();

describe('K-Nearest Neighbors', () => {
  test('can instantiate', () => {
    const knn = new KNN(3);
    expect(knn).toBeDefined();
  });
});
