import collections
from typing import List


def sortItems(n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def get_top_order(graph, indegree):
            top_order = []
            stack = [node for node in range(len(graph)) if indegree[node] == 0]
            while stack:
                v = stack.pop()
                top_order.append(v)
                for u in graph[v]:
                    indegree[u] -= 1
                    if indegree[u] == 0:
                        stack.append(u)
            return top_order if len(top_order) == len(graph) else []

        for u in range(len(group)):
            if group[u] == -1:
                group[u] = m
                m+=1

        graph_items = [[] for _ in range(n)]
        indegree_items = [0] * n
        graph_groups = [[] for _ in range(m)]
        indegree_groups = [0] * m        
        for u in range(n):
            for v in beforeItems[u]:                
                graph_items[v].append(u)
                indegree_items[u] += 1
                if group[u]!=group[v]:
                    graph_groups[group[v]].append(group[u])
                    indegree_groups[group[u]] += 1                    

        item_order = get_top_order(graph_items, indegree_items)
        group_order = get_top_order(graph_groups, indegree_groups)
        if not item_order or not group_order: return []

        order_within_group = collections.defaultdict(list)
        for v in item_order:
            order_within_group[group[v]].append(v)

        res = []
        for group in group_order:
            res += order_within_group[group]
        return res