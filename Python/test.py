class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

def wordSearch2(board, words):
    root = TrieNode()
    for word in words:
        root.addWord(word)
    ROW, COL = len(board), len(board[0])
    res,visited = set(), set()
    def dfs(r,c,node,word):
        if r<0 or c<0 or r==ROW or c==COL or board[r][c] not in node.children or (r,c) in visited:
            return
        visited.add((r,c))
        node = node.children[board[r][c]]
        word+= board[r][c]
        if node.isWord:
            res.add(word)
        dfs(r+1,c,node,word)
        dfs(r-1,c,node,word)
        dfs(r,c+1,node,word)
        dfs(r,c-1,node,word)
        visited.remove((r,c))
    for r in range(ROW):
        for c in range(COL):
            dfs(r,c,root,"")
    return list(res)