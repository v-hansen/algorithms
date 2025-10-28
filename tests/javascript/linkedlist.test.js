const fs = require('fs');
const path = require('path');

const algoDir = path.join(__dirname, '../../linked-list');
const possibleFiles = ['linked_list.js', 'linked-list.js', 'linkedList.js'];
let code = null;

for (const file of possibleFiles) {
  try {
    code = fs.readFileSync(path.join(algoDir, file), 'utf8');
    break;
  } catch (e) {}
}

if (!code) throw new Error('Could not find implementation file');

const func = new Function(code + '; return LinkedList;');
const LinkedList = func();

describe('Linked List', () => {
  test('append and display', () => {
    const ll = new LinkedList();
    ll.append(1);
    ll.append(2);
    ll.append(3);
    expect(ll.display()).toEqual([1, 2, 3]);
  });
});
