import collections
from math import sqrt

def maximumDetonation(bombs) -> int:
        adj = collections.defaultdict(list)
        for i in range(len(bombs)):
            for j in range(i+1, len(bombs)):
                x1,y1,r1 = bombs[i]
                x2,y2,r2 = bombs[j]
                dist = sqrt((x1 - x2)**2 + (y1 - y2)**2)
                if dist <= r1:
                    adj[i].append(j)
                if dist <= r2:
                    adj[j].append(i)
                
        def dfs(i, visited):
            if i in visited:
                return 0
            visited.add(i)
            for nei in adj[i]:
                dfs(nei, visited)
            return len(visited)
        
        res = 0
        for i in range(len(bombs)):
            res = max(res, dfs(i, set()))
        return res