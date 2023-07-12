def eventualSafeNodes(graph):
        def explore(i):
            visited[i] = 0
            for v in graph[i]:
                if visited[v] == 0 or (visited[v] == -1 and explore(v)): return True
            visited[i] = 1
            res.append(i)
            return False
        visited, res = [-1] * len(graph), []
        for i in range(len(graph)):
            if visited[i] == -1: explore(i)
        return sorted(res)
    
    
def eventualSafeNodes(graph):
        safe = {}
        n = len(graph)
        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i] = False
            for nei in graph[i]:
                if not dfs(nei):
                    return False
            safe[i] = True
            return True
        
        ans = []
        for i in range(n):
            if dfs(i):
                ans.append(i)
        return ans

print(eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))