from collections import defaultdict
import heapq
from typing import List


def minimumCost(source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
    mapping = defaultdict(list)
    for src, dest, cst in zip(original, changed, cost):
        mapping[src].append((dest, cst))
 
  
    def shortest_path(src):
        sortest_path = {}
        heap = [(0, src)]
        while heap:
            cst, dest = heapq.heappop(heap)
            if dest in sortest_path:
                continue
            sortest_path[dest] = cst
            for nei, c in mapping[dest]:
                heapq.heappush(heap, (c+cst, nei))
        return sortest_path
    

    shortest_path_maps = {src: shortest_path(src) for src in set(source)}
    min_cost = 0
    for src, dest in zip(source, target):
        if dest not in shortest_path_maps[src]:
            return -1
        min_cost += shortest_path_maps[src][dest]
    return min_cost
   
    
print(minimumCost("abcd", "acbe", ["a","b","c","c","e","d"], ["b","c","b","e","b","e"], [2,5,5,1,2,20]))