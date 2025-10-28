const fs = require('fs');
const path = require('path');

const algoDir = path.join(__dirname, '../../trie');
const possibleFiles = ['trie.js'];
let code = null;

for (const file of possibleFiles) {
  try {
    code = fs.readFileSync(path.join(algoDir, file), 'utf8');
    break;
  } catch (e) {}
}

if (!code) throw new Error('Could not find implementation file');

const func = new Function(code + '; return Trie;');
const Trie = func();

describe('Trie', () => {
  test('insert and search', () => {
    const trie = new Trie();
    trie.insert("hello");
    trie.insert("world");
    expect(trie.search("hello")).toBe(true);
    expect(trie.search("hell")).toBe(false);
  });
});
