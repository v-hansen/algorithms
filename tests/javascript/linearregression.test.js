const fs = require('fs');
const path = require('path');

const algoDir = path.join(__dirname, '../../linear-regression');
const possibleFiles = ['linear_regression.js', 'linear-regression.js', 'linearRegression.js'];
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
const func = new Function(code + '; return LinearRegression;');
console.log = originalLog;
const LinearRegression = func();

describe('Linear Regression', () => {
  test('can instantiate', () => {
    const lr = new LinearRegression();
    expect(lr).toBeDefined();
  });
});
