import collections
import heapq
from typing import List

def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            src, dest = edges[i]
            prob = succProb[i]
            adj[src].append([dest, prob])
            adj[dest].append([src, prob])
            
        pq = [(-1, start)]
        visited = set()
        
        while pq:
            prob, curr = heapq.heappop(pq)
            visited.add(curr)
            
            if curr == end:
                return prob * -1
            
            for nei, edgeProb in adj[curr]:
                if nei not in visited:
                    heapq.heappush(pq, ((prob * edgeProb), nei))
        
        return 0