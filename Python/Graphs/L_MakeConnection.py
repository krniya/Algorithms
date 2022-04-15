def makeConnection(connections, n):
        if len(connections) < n - 1:
            return -1
        visited = set()
        graph = [[] for _ in range(n)]
        count = 0
        def dfs(i):
            visited.add(i)
            for next_node in graph[i]:
                if next_node not in visited:
                    dfs(next_node)

        for connection in connections:
            graph[connection[0]].append(connection[1])
            graph[connection[1]].append(connection[0])
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count - 1

print(makeConnection([[0,1],[0,2],[1,2]],4))

# To connect n seprate components we need minimum n-1 connections to connect them all, find all the seprate components and return -1 of it

    