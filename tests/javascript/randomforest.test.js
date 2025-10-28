const fs = require('fs');
const path = require('path');

const algoDir = path.join(__dirname, '../../random-forest');
const possibleFiles = ['random_forest.js', 'random-forest.js', 'randomForest.js'];
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
const func = new Function(code + '; return RandomForest;');
console.log = originalLog;
const RandomForest = func();

describe('Random Forest', () => {
  test('can instantiate', () => {
    const rf = new RandomForest();
    expect(rf).toBeDefined();
  });
});
