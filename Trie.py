# This code implements a Trie (prefix tree) data structure with methods to insert words, search for exact words, and check for prefixes.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self._search_node(word)
        return node is not None and node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        return self._search_node(prefix) is not None

    def _search_node(self, prefix: str):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node


# Test.py
trie = Trie()

output = []
output.append(None)  
output.append(trie.insert("apple"))   
output.append(trie.search("apple"))   
output.append(trie.search("app"))     
output.append(trie.startsWith("app")) 
output.append(trie.insert("app"))     
output.append(trie.search("app"))     

print(output)
