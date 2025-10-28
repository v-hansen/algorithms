const fs = require('fs');
const path = require('path');

const algoDir = path.join(__dirname, '../../k-means-clustering');
const possibleFiles = ['k_means.js', 'k_means_clustering.js', 'k-means-clustering.js'];
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
const func = new Function(code + '; return KMeans;');
console.log = originalLog;
const KMeans = func();

describe('K-Means Clustering', () => {
  test('can instantiate', () => {
    const kmeans = new KMeans(2);
    expect(kmeans).toBeDefined();
  });
});
