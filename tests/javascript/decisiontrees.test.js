const fs = require('fs');
const path = require('path');

const algoDir = path.join(__dirname, '../../decision-trees');
const possibleFiles = ['decision_tree.js', 'decision_trees.js', 'decision-trees.js'];
let code = null;

for (const file of possibleFiles) {
  try {
    code = fs.readFileSync(path.join(algoDir, file), 'utf8');
    break;
  } catch (e) {}
}

if (!code) throw new Error('Could not find implementation file');

// Suppress console output
const originalLog = console.log;
console.log = () => {};

const func = new Function(code + '; return DecisionTree;');
const DecisionTree = func();

console.log = originalLog;

describe('Decision Trees', () => {
  test('can instantiate', () => {
    const dt = new DecisionTree();
    expect(dt).toBeDefined();
  });
});
