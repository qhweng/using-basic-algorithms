## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
    def insert(self, char):
        # Add a child node to starting TrieNode
        if char not in self.children:
            self.children[char] = TrieNode()

    def suffixes(self, suffix = ''):
        # Collects the suffix for all complete words below starting TrieNode
        suff = []
             
        if self.is_word:
            suff += [suffix]

        # Recursively find the suffix by adding the characters until end node
        for child in self.children:
             suff += self.children[child].suffixes(suffix + child)

        return suff


## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        curr_node = self.root

        if word is None:
            return
        
        for char in word:
            curr_node.insert(char)
            curr_node = curr_node.children[char]

        curr_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        curr_node = self.root

        if prefix is None:
            return curr_node
        
        for char in prefix:
            if char not in curr_node.children:
                return None
            curr_node = curr_node.children[char]

        return curr_node


def test():
    # Test case: normal values
    MyTrie = Trie()
    wordList = [
        "ant", "anthology", "antagonist", "antonym", 
        "fun", "function", "factory", 
        "trie", "trigger", "trigonometry", "tripod"
    ]
    
    for word in wordList:
        MyTrie.insert(word)

    prefixNode = MyTrie.find("f")
    assert prefixNode.suffixes() == ['un', 'unction', 'actory']

    # Test case: no values, empty list
    NextTrie = Trie()
    NextTrie.insert("")

    prefixNode = NextTrie.find("")
    assert prefixNode.suffixes() == [""]

    # Test case: None value
    LastTrie = Trie()
    LastTrie.insert(None)

    prefixNode = NextTrie.find(None)
    assert prefixNode.suffixes() == [""]
    

test()
# print("Finished testing")
