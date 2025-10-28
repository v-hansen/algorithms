const fs = require('fs');
const path = require('path');

const algoDir = path.join(__dirname, '../../hash-table');
const possibleFiles = ['hash_table.js', 'hash-table.js', 'hashTable.js'];
let code = null;

for (const file of possibleFiles) {
  try {
    code = fs.readFileSync(path.join(algoDir, file), 'utf8');
    break;
  } catch (e) {}
}

if (!code) throw new Error('Could not find implementation file');

const func = new Function(code + '; return HashTable;');
const HashTable = func();

describe('Hash Table', () => {
  test('put and get', () => {
    const ht = new HashTable();
    ht.put("key1", "value1");
    ht.put("key2", "value2");
    expect(ht.get("key1")).toBe("value1");
    expect(ht.get("key2")).toBe("value2");
  });
});
