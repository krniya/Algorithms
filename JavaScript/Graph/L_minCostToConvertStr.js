var minimumCost = function (source, target, original, changed, cost) {
    const CHAR_COUNT = 26;
    const INF = Number.MAX_SAFE_INTEGER / 2;

    const buildConversionGraph = (original, changed, cost) => {
        const graph = Array(CHAR_COUNT)
            .fill()
            .map(() => Array(CHAR_COUNT).fill(INF));
        for (let i = 0; i < CHAR_COUNT; i++) {
            graph[i][i] = 0;
        }
        for (let i = 0; i < cost.length; i++) {
            const from = original[i].charCodeAt(0) - "a".charCodeAt(0);
            const to = changed[i].charCodeAt(0) - "a".charCodeAt(0);
            graph[from][to] = Math.min(graph[from][to], cost[i]);
        }
        return graph;
    };

    const optimizeConversionPaths = (graph) => {
        for (let k = 0; k < CHAR_COUNT; k++) {
            for (let i = 0; i < CHAR_COUNT; i++) {
                if (graph[i][k] < INF) {
                    for (let j = 0; j < CHAR_COUNT; j++) {
                        if (graph[k][j] < INF) {
                            graph[i][j] = Math.min(graph[i][j], graph[i][k] + graph[k][j]);
                        }
                    }
                }
            }
        }
    };

    const computeTotalConversionCost = (source, target, graph) => {
        let totalCost = 0;
        for (let i = 0; i < source.length; i++) {
            const sourceChar = source.charCodeAt(i) - "a".charCodeAt(0);
            const targetChar = target.charCodeAt(i) - "a".charCodeAt(0);
            if (sourceChar !== targetChar) {
                if (graph[sourceChar][targetChar] === INF) {
                    return -1;
                }
                totalCost += graph[sourceChar][targetChar];
            }
        }
        return totalCost;
    };

    const conversionGraph = buildConversionGraph(original, changed, cost);
    optimizeConversionPaths(conversionGraph);
    return computeTotalConversionCost(source, target, conversionGraph);
};
