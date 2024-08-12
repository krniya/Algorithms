var minDays = function (grid) {
    // Helper function to perform Depth-First Search (DFS) to explore the island
    function dfs(grid, visited, i, j) {
        const m = grid.length,
            n = grid[0].length;
        // Check boundaries and whether the cell is already visited or is water
        if (i < 0 || j < 0 || i >= m || j >= n || grid[i][j] === 0 || visited[i][j]) return;
        visited[i][j] = true; // Mark the cell as visited
        // Recursively visit all 4 directions
        dfs(grid, visited, i + 1, j);
        dfs(grid, visited, i - 1, j);
        dfs(grid, visited, i, j + 1);
        dfs(grid, visited, i, j - 1);
    }

    // Function to count the number of islands (connected groups of 1's)
    function countIslands(grid) {
        const m = grid.length,
            n = grid[0].length;
        const visited = Array.from({ length: m }, () => Array(n).fill(false));
        let count = 0;

        // Iterate through the grid to find and count each island
        for (let i = 0; i < m; ++i) {
            for (let j = 0; j < n; ++j) {
                // If we find a land cell that is not visited, start a new DFS
                if (grid[i][j] === 1 && !visited[i][j]) {
                    count++;
                    dfs(grid, visited, i, j); // Explore the island
                }
            }
        }
        return count;
    }

    // Function to determine the minimum number of days to disconnect the island
    if (countIslands(grid) !== 1) return 0;

    const m = grid.length,
        n = grid[0].length;

    // Step 2: Try removing one land cell
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (grid[i][j] === 1) {
                grid[i][j] = 0; // Remove the land cell
                // Check if removing this cell disconnects the grid
                if (countIslands(grid) !== 1) return 1;
                grid[i][j] = 1; // Restore the land cell
            }
        }
    }

    // Step 3: If removing one cell isn't enough, return 2 (as it is guaranteed to be sufficient)
    return 2;
};
