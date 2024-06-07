class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True
    
    def search(self, word):
        node = self.root
        prefix = ''
        for char in word:
            if char not in node.children:
                return word
            prefix += char
            if node.children[char].isEnd:
                return prefix
            node = node.children[char]
        return word

class Solution:
    def replaceWords(self, dictionary, sentence):
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        
        result = []
        for word in sentence.split():
            result.append(trie.search(word))
        
        return ' '.join(result)