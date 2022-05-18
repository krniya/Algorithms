import collections


def criticalConnections(n: int, connections):
        def dfs(rank, curr, prev):
            low[curr], result = rank, []
            for neighbor in edges[curr]:
                if neighbor == prev: continue
                if not low[neighbor]:
                    result += dfs(rank + 1, neighbor, curr)
                low[curr] = min(low[curr], low[neighbor])
                if low[neighbor] >= rank + 1:
                    result.append([curr, neighbor])
            return result

        low, edges = [0] * n, collections.defaultdict(list)
        for u, v in connections:
            edges[u].append(v)
            edges[v].append(u)

        return dfs(1, 0, -1)