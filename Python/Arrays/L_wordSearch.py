def exist(board, word):
    m,n = len(board), len(board[0])
    path = set()
                
    def dfs(i,j,l):
        if len(word) == l:
            return True
        if (i < 0 or j < 0 or i >= m or j >= n or word[l] != board[i][j] or (i,j) in path):
            return False
        path.add((i,j))
        res = (dfs(i+1, j, l+1) or dfs(i, j+1, l+1) or dfs(i-1, j, l+1) or dfs(i, j-1, l+1))
        path.remove((i,j))
        return res
        
    for i in range(m):
        for j in range(n):
            if dfs(i,j,0): return True
    return False