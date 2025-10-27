struct Node {
    data: i32,
    next: Option<Box<Node>>,
}

struct LinkedList {
    head: Option<Box<Node>>,
}

impl LinkedList {
    fn new() -> Self {
        LinkedList { head: None }
    }
    
    fn append(&mut self, data: i32) {
        let new_node = Box::new(Node { data, next: None });
        
        match &mut self.head {
            None => self.head = Some(new_node),
            Some(head) => {
                let mut current = head;
                while current.next.is_some() {
                    current = current.next.as_mut().unwrap();
                }
                current.next = Some(new_node);
            }
        }
    }
    
    fn prepend(&mut self, data: i32) {
        let new_node = Box::new(Node {
            data,
            next: self.head.take(),
        });
        self.head = Some(new_node);
    }
    
    fn display(&self) {
        let mut current = &self.head;
        while let Some(node) = current {
            print!("{} -> ", node.data);
            current = &node.next;
        }
        println!("null");
    }
    
    fn search(&self, data: i32) -> bool {
        let mut current = &self.head;
        while let Some(node) = current {
            if node.data == data {
                return true;
            }
            current = &node.next;
        }
        false
    }
}

fn main() {
    let mut list = LinkedList::new();
    list.append(1);
    list.append(2);
    list.prepend(0);
    list.display();
    println!("Search 2: {}", list.search(2));
}