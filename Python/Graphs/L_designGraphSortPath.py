import heapq
from typing import List


class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        # Adjacency list to represent the graph
        self.adjacencyList = [[] for _ in range(n)]

        # Constructor to initialize the graph with nodes and edges
        for edge in edges:
            self.adjacencyList[edge[0]].append((edge[1], edge[2]))

    # Add a new edge to the graph
    def addEdge(self, edge: List[int]):
        self.adjacencyList[edge[0]].append((edge[1], edge[2]))

    # Find the shortest path between two nodes using Dijkstra's algorithm
    def shortestPath(self, node1: int, node2: int) -> int:
        return self.dijkstra(node1, node2)

    # Dijkstra's algorithm to find the shortest path
    def dijkstra(self, start: int, end: int) -> int:
        n = len(self.adjacencyList)
        distances = [float('inf')] * n
        distances[start] = 0

        # Priority queue to efficiently retrieve the node with the minimum distance
        priorityQueue = [(0, start)]

        while priorityQueue:
            currentCost, currentNode = heapq.heappop(priorityQueue)

            # Skip if a shorter path has already been found
            if currentCost > distances[currentNode]:
                continue

            # If found the target node then return the cost
            if currentNode == end:
                return currentCost

            # Explore neighbors and update distances
            for edge in self.adjacencyList[currentNode]:
                neighbor, edgeLength = edge
                newRouteCost = edgeLength + distances[currentNode]

                # Update distance if a shorter route is found
                if distances[neighbor] > newRouteCost:
                    distances[neighbor] = newRouteCost
                    heapq.heappush(priorityQueue, (newRouteCost, neighbor))

        # Return the minimum distance or -1 if no path exists
        return -1 if distances[end] == float('inf') else distances[end]
    