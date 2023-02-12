from typing import List
from collections import defaultdict
from math import ceil

def minimumFuelCost(roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(list)
        for x, y in roads:
            graph[x].append(y)
            graph[y].append(x)
        ans = 0
        
        def dfs(i, prev, people = 1):
            for x in graph[i]:
                if x == prev: continue
                people += dfs(x, i)
            nonlocal ans
            ans += (int(ceil(people / seats)) if i else 0)
            return people
        
        dfs(0, 0)
        return ans