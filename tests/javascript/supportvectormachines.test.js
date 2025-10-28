const fs = require('fs');
const path = require('path');

const algoDir = path.join(__dirname, '../../support-vector-machines');
const possibleFiles = ['support_vector_machines.js', 'support-vector-machines.js', 'svm.js'];
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
const func = new Function(code + '; return SVM;');
console.log = originalLog;
const SVM = func();

describe('Support Vector Machines', () => {
  test('can instantiate', () => {
    const svm = new SVM();
    expect(svm).toBeDefined();
  });
});
