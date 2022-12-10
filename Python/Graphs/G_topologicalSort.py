def topoSort(V, adj):
        # Code here
        visited = set()
        stack = []
        def dfs(node):
            if node in visited: return
            visited.add(node)
            for n in adj[node]:
                dfs(n)
            stack.append(node)
        for i in range(V):
            dfs(i)
        return stack[::-1]

print(topoSort(6, [[],[],[3],[1],[0,1],[0,2]]))