def validGraphTree(n, edges):
    adj = {i:[] for i in range(n)}
    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)
    visit = set()
    def dfs(n,prev):
        if n in visit:
            return False
        visit.add(n)
        for i in adj[n]:
            if i == prev:
                continue
            if not dfs(i, n):
                return False
        return True
    return dfs(0,-1) and len(visit) == n