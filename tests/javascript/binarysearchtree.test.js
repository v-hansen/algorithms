const fs = require('fs');
const path = require('path');

const algoDir = path.join(__dirname, '../../binary-search-tree');
const possibleFiles = ['binary_search_tree.js', 'binary-search-tree.js', 'binarySearchTree.js'];
let code = null;

for (const file of possibleFiles) {
  try {
    code = fs.readFileSync(path.join(algoDir, file), 'utf8');
    break;
  } catch (e) {}
}

if (!code) throw new Error('Could not find implementation file');

const func = new Function(code + '; return BST;');
const BST = func();

describe('Binary Search Tree', () => {
  test('insert and search', () => {
    const bst = new BST();
    bst.insert(50);
    bst.insert(30);
    bst.insert(70);
    expect(bst.search(30)).toBeTruthy();
    expect(bst.search(100)).toBeFalsy();
  });
});
