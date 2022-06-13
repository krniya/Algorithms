class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word = True


    def search(self, word):
        
        def dfs(j,node):
            curr = node
            for i in range(j,len(word)):
                ch = word[i]
                if ch == ".":
                    for child in curr.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if ch not in curr.children:
                        return False
                    curr = curr.children[ch]
            return curr.word
        return dfs(0,self.root)