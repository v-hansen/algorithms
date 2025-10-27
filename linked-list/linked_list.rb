class Node
  attr_accessor :data, :next
  def initialize(data)
    @data, @next = data, nil
  end
end

class LinkedList
  def initialize
    @head = nil
  end
  
  def append(data)
    new_node = Node.new(data)
    if @head.nil?
      @head = new_node
    else
      current = @head
      current = current.next while current.next
      current.next = new_node
    end
  end
  
  def display
    current = @head
    while current
      print "#{current.data} -> "
      current = current.next
    end
    puts "nil"
  end
end

ll = LinkedList.new
[1, 2, 3].each { |x| ll.append(x) }
ll.display