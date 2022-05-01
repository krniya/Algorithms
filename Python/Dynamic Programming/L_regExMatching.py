def isMatch(s, p):
    table = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
    table[0][0] = True
    for i in range(2, len(p) + 1):
        table[i][0] = table[i - 2][0] and p[i - 1] == '*'
    for i in range(1, len(p) + 1):
        for j in range(1, len(s) + 1):
            if p[i - 1] != "*":
                table[i][j] = table[i - 1][j - 1] and (p[i - 1] == s[j - 1] or p[i - 1] == '.')
            else:
                table[i][j] = table[i - 2][j] or table[i - 1][j]
                if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                    table[i][j] |= table[i][j - 1]
    return table[-1][-1]

def isMatch(s, p):
        cache = {}
        def dfs(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            match = (i < len(s) and (s[i] == p[j] or p[j] == "." ))
            if (j + 1) < len(p) and p[j+1] == "*":
                cache[(i,j)] = dfs(i,j+2) or (match and dfs(i+1, j))
                return cache[(i,j)]
            if match:
                cache[(i,j)] = dfs(i+1,j+1)
                return cache[(i,j)]
            cache[(i,j)] = False
            return False
        
        return dfs(0,0)
