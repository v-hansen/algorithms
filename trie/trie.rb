class TrieNode
  attr_accessor :children, :is_end
  def initialize
    @children = {}
    @is_end = false
  end
end

class Trie
  def initialize
    @root = TrieNode.new
  end
  
  def insert(word)
    node = @root
    word.each_char do |char|
      node.children[char] ||= TrieNode.new
      node = node.children[char]
    end
    node.is_end = true
  end
  
  def search(word)
    node = @root
    word.each_char do |char|
      return false unless node.children[char]
      node = node.children[char]
    end
    node.is_end
  end
end

trie = Trie.new
trie.insert("hello")
puts trie.search("hello")