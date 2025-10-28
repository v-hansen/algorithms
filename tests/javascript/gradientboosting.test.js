const fs = require('fs');
const path = require('path');

const algoDir = path.join(__dirname, '../../gradient-boosting');
const possibleFiles = ['gradient_boosting.js', 'gradient-boosting.js', 'gradientBoosting.js'];
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
const func = new Function(code + '; return GradientBoosting;');
console.log = originalLog;
const GradientBoosting = func();

describe('Gradient Boosting', () => {
  test('can instantiate', () => {
    const gb = new GradientBoosting();
    expect(gb).toBeDefined();
  });
});
