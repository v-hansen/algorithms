package main
import "fmt"

type Node struct {
    data int
    next *Node
}

type LinkedList struct {
    head *Node
}

func (ll *LinkedList) Append(data int) {
    newNode := &Node{data: data}
    
    if ll.head == nil {
        ll.head = newNode
        return
    }
    
    current := ll.head
    for current.next != nil {
        current = current.next
    }
    current.next = newNode
}

func (ll *LinkedList) Prepend(data int) {
    newNode := &Node{data: data, next: ll.head}
    ll.head = newNode
}

func (ll *LinkedList) Display() {
    current := ll.head
    for current != nil {
        fmt.Print(current.data, " -> ")
        current = current.next
    }
    fmt.Println("nil")
}

func (ll *LinkedList) Search(data int) bool {
    current := ll.head
    for current != nil {
        if current.data == data {
            return true
        }
        current = current.next
    }
    return false
}

func main() {
    ll := &LinkedList{}
    ll.Append(1)
    ll.Append(2)
    ll.Prepend(0)
    ll.Display()
    fmt.Printf("Search 2: %t\n", ll.Search(2))
}