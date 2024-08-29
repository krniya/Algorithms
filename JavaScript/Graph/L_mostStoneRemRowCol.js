/**
 * @param {number[][]} stones
 * @return {number}
 */
var removeStones = function (stones) {
    const rows = new Map(); // Map to track which columns are occupied by stones in each row
    const cols = new Map(); // Map to track which rows are occupied by stones in each column

    // Build the adjacency maps for rows and columns
    for (const [r, c] of stones) {
        if (!rows.has(r)) rows.set(r, new Set());
        if (!cols.has(c)) cols.set(c, new Set());
        rows.get(r).add(c);
        cols.get(c).add(r);
    }

    const visited = new Set(); // Set to track visited stones

    // Depth-First Search function to visit connected stones
    const visit = (i, j) => {
        const key = `${i}-${j}`;
        if (visited.has(key)) return; // If already visited, return
        visited.add(key); // Mark the current stone as visited

        // Visit all stones in the same row
        const adjRow = rows.get(i);
        for (const col of adjRow) {
            visit(i, col);
        }
        // Visit all stones in the same column
        const adjCol = cols.get(j);
        for (const row of adjCol) {
            visit(row, j);
        }
    };

    let remainingStones = 0; // Counter for number of connected components

    // Iterate through each stone to find connected components
    for (const [r, c] of stones) {
        const key = `${r}-${c}`;
        if (visited.has(key)) continue; // Skip if already visited
        visit(r, c); // Start a DFS from this stone
        remainingStones++; // Increment the count of connected components
    }

    // Return the maximum number of stones that can be removed
    return stones.length - remainingStones;
};
