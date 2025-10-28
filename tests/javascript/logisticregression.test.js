const fs = require('fs');
const path = require('path');

const algoDir = path.join(__dirname, '../../logistic-regression');
const possibleFiles = ['logistic_regression.js', 'logistic-regression.js', 'logisticRegression.js'];
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
const func = new Function(code + '; return LogisticRegression;');
console.log = originalLog;
const LogisticRegression = func();

describe('Logistic Regression', () => {
  test('can instantiate', () => {
    const lr = new LogisticRegression();
    expect(lr).toBeDefined();
  });
});
