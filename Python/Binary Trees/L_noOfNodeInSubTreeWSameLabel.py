from typing import List
from collections import Counter, defaultdict

def countSubTrees(n: int, edges: List[List[int]], labels: str) -> List[int]:
        def dfs(node: int):
            cnt = Counter()
            if node not in seen:
                cnt[labels[node]] += 1 
                seen.add(node)
                for child in g.get(node, []):
                    cnt += dfs(child)
                ans[node] = cnt[labels[node]]
            return cnt
        
        g, ans, seen = defaultdict(list), [0] * n, set()
        for a, b in edges:
            g[a] += [b]
            g[b] += [a]
        dfs(0)
        return ans