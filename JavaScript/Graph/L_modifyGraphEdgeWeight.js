/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} source
 * @param {number} destination
 * @param {number} target
 * @return {number[][]}
 */
var modifiedGraphEdges = function (n, edges, source, destination, target) {
    class PriorityQueue {
        constructor() {
            this.elements = [];
        }

        enqueue(element, priority) {
            this.elements.push({ element, priority });
            this.elements.sort((a, b) => a.priority - b.priority);
        }

        dequeue() {
            return this.elements.shift();
        }

        isEmpty() {
            return this.elements.length === 0;
        }
    }

    const adjacencyList = Array.from({ length: n }, () => []);
    for (let i = 0; i < edges.length; i++) {
        const [nodeA, nodeB] = edges[i];
        adjacencyList[nodeA].push([nodeB, i]);
        adjacencyList[nodeB].push([nodeA, i]);
    }

    const distances = Array.from({ length: n }, () => [Infinity, Infinity]);
    distances[source] = [0, 0];

    runDijkstra(adjacencyList, edges, distances, source, 0, 0);
    const difference = target - distances[destination][0];
    if (difference < 0) return [];

    runDijkstra(adjacencyList, edges, distances, source, difference, 1);
    if (distances[destination][1] < target) return [];

    for (const edge of edges) {
        if (edge[2] === -1) edge[2] = 1;
    }

    return edges;

    function runDijkstra(adjacencyList, edges, distances, source, difference, run) {
        const pq = new PriorityQueue();
        pq.enqueue(source, 0);
        distances[source][run] = 0;

        while (!pq.isEmpty()) {
            const { element: currentNode, priority: currentDistance } = pq.dequeue();

            if (currentDistance > distances[currentNode][run]) continue;

            for (const [nextNode, edgeIndex] of adjacencyList[currentNode]) {
                let weight = edges[edgeIndex][2];
                if (weight === -1) weight = 1;

                if (run === 1 && edges[edgeIndex][2] === -1) {
                    const newWeight =
                        difference + distances[nextNode][0] - distances[currentNode][1];
                    if (newWeight > weight) {
                        edges[edgeIndex][2] = weight = newWeight;
                    }
                }

                if (distances[nextNode][run] > distances[currentNode][run] + weight) {
                    distances[nextNode][run] = distances[currentNode][run] + weight;
                    pq.enqueue(nextNode, distances[nextNode][run]);
                }
            }
        }
    }
};
