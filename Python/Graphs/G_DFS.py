from collections import defaultdict


class Graph:
    __slots__ = ['graph']

    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=" ")
        for neigh in self.graph[v]:
            if neigh not in visited:
                self.DFSUtil(neigh, visited)

    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.DFS(2)
