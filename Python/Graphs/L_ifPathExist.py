def validPath(n: int, edges, source: int, destination: int) -> bool:
        parent = [i for i in range(n)]
        rank = [1] * (n)
        
        def find(n):
            if n == parent[n]: return n
            parent[n] = find(parent[n])
            return parent[n]
        
        # Union
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for n1, n2 in edges:
            union(n1, n2)

        find(source)
        find(destination)   
        return parent[source] == parent[destination]

def validPath(n: int, edges, start: int, end: int) -> bool:
        queue = [start]
        graph = {}
        for vertex in range(n):
            graph[vertex] = []
        
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        visited = {start}
        
        while len(queue) != 0:
            node = queue.pop(0)
            if node == end:
                return True
            
            for vertex in graph[node]:
                if vertex not in visited:
                    visited.add(vertex)
                    queue.append(vertex)
        
        return False

print(validPath(10, [[2,6],[4,7],[1,2],[3,5],[7,9],[6,4],[9,8],[0,1],[3,0]],3,5))