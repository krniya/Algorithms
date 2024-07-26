def findTheCity(n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        distance: list[list[int]] = [[float("inf") for _ in range(n)] for _ in range(n)]
        for node in range(n):
            distance[node][node] = 0  # distance to itself is 0

        # The distance between nodes which are connected temporary distance between them
        for node1, node2, dist in edges:
            distance[node1][node2] = dist
            distance[node2][node1] = dist

        for midle in range(n):
            for source in range(n):
                for destination in range(n):
                    distance[source][destination] = min(
                        distance[source][destination], distance[source][midle] + distance[midle][destination]
                    )  # the minimum distance is either current value or new value with path that goes through midle

        minimum_number: int = n
        res: int = None

        for source in range(n):
            source_count = 0
            for destination in range(n):
                if distance[source][destination] <= distanceThreshold:
                    source_count += 1

            if source_count <= minimum_number:  # as in dijkstra when number equal we choose greater node
                minimum_number = source_count
                res = source

        return res