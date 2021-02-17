from collections import defaultdict


class Graph:
    def __init__(self, vertices) -> None:
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        for node in range(self.V):
            if self.isCyclicUtil(node, visited, recStack):
                return True
        return False

    def isCyclicUtil(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True
        for neigh in self.graph[v]:
            if visited[neigh] == False:
                if self.isCyclicUtil(neigh, visited, recStack):
                    return True
                elif recStack[neigh] == True:
                    return False
        recStack[v] = False
        return False


g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
if g.isCyclic():
    print("Graph has a cycle")
else:
    print("Graph has no cycle")
