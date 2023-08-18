import collections
from typing import List


def maximalNetworkRank(n: int, roads: List[List[int]]) -> int:
    graph = collections.defaultdict(set)
    
    for city1, city2 in roads:
        graph[city1].add(city2)
        graph[city2].add(city1)
    
    res = 0
    
    for city1 in range(n):
        for city2 in range(city1 + 1, n):
            
            has_connection = 1 if city1 in graph[city2] else 0
            
            city1_connection = len(graph[city1])
            city2_connection = len(graph[city2])
            
            res = max(res, city1_connection + city2_connection - has_connection)
    
    return res