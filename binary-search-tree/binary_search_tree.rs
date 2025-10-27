use std::rc::Rc;
use std::cell::RefCell;

type NodeRef = Rc<RefCell<Node>>;

struct Node {
    data: i32,
    left: Option<NodeRef>,
    right: Option<NodeRef>,
}

struct BST {
    root: Option<NodeRef>,
}

impl BST {
    fn new() -> Self {
        BST { root: None }
    }
    
    fn insert(&mut self, data: i32) {
        self.root = Self::insert_rec(self.root.take(), data);
    }
    
    fn insert_rec(node: Option<NodeRef>, data: i32) -> Option<NodeRef> {
        match node {
            None => Some(Rc::new(RefCell::new(Node {
                data,
                left: None,
                right: None,
            }))),
            Some(n) => {
                if data < n.borrow().data {
                    n.borrow_mut().left = Self::insert_rec(n.borrow_mut().left.take(), data);
                } else {
                    n.borrow_mut().right = Self::insert_rec(n.borrow_mut().right.take(), data);
                }
                Some(n)
            }
        }
    }
    
    fn search(&self, data: i32) -> bool {
        Self::search_rec(&self.root, data)
    }
    
    fn search_rec(node: &Option<NodeRef>, data: i32) -> bool {
        match node {
            None => false,
            Some(n) => {
                let node_data = n.borrow().data;
                if node_data == data {
                    true
                } else if data < node_data {
                    Self::search_rec(&n.borrow().left, data)
                } else {
                    Self::search_rec(&n.borrow().right, data)
                }
            }
        }
    }
}

fn main() {
    let mut bst = BST::new();
    for val in [50, 30, 70, 20, 40] {
        bst.insert(val);
    }
    println!("{}", bst.search(40));
}