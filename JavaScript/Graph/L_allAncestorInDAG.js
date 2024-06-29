var getAncestors = function (n, edges) {
    let res = Array.from({ length: n }, () => []);
    let graph = Array.from({ length: n }, () => []);

    for (let edge of edges) {
        graph[edge[0]].push(edge[1]);
    }

    for (let i = 0; i < n; i++) {
        dfs(graph, i, i, res, Array(n).fill(false));
    }

    for (let i = 0; i < n; i++) {
        res[i].sort((a, b) => a - b);
    }

    return res;
};

function dfs(graph, parent, curr, res, visit) {
    visit[curr] = true;
    for (let dest of graph[curr]) {
        if (!visit[dest]) {
            res[dest].push(parent);
            dfs(graph, parent, dest, res, visit);
        }
    }
}
