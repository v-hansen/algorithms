class Node
  attr_accessor :data, :left, :right
  def initialize(data)
    @data, @left, @right = data, nil, nil
  end
end

class BST
  def initialize
    @root = nil
  end
  
  def insert(data)
    @root = insert_node(@root, data)
  end
  
  def insert_node(node, data)
    return Node.new(data) unless node
    if data < node.data
      node.left = insert_node(node.left, data)
    else
      node.right = insert_node(node.right, data)
    end
    node
  end
  
  def search(data)
    search_node(@root, data)
  end
  
  def search_node(node, data)
    return node if !node || node.data == data
    data < node.data ? search_node(node.left, data) : search_node(node.right, data)
  end
end

bst = BST.new
[50, 30, 70, 20, 40].each { |x| bst.insert(x) }
puts bst.search(40) ? "Found" : "Not found" 