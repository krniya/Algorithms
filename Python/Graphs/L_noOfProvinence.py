def findCircleNum(isConnected):
        n = len(isConnected)
        seen = set()
        def dfs(node):
            for nei, adj in enumerate(isConnected[node]):
                if adj and nei not in seen:
                    seen.add(nei)
                    dfs(nei)
    
        ans = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                ans += 1
        return ans

print(findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))