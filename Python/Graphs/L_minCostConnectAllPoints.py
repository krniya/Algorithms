import heapq


def minCostConnectPoints(points) -> int:
        n = len(points)
        adjList = {i:[] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1- x2) + abs(y1 - y2)
                adjList[i].append([dist, j])
                adjList[j].append([dist, i])
        res = 0
        minH = [[0, 0]]
        visited = set()
        while len(visited) < n:
            cost, node = heapq.heappop(minH)
            if node in visited:
                continue
            res += cost
            visited.add(node)
            for dist, nei in adjList[node]:
                if nei not in visited:
                    heapq.heappush(minH, [dist, nei])
        return res

