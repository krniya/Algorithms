/**
 * @param {number[][]} grid1
 * @param {number[][]} grid2
 * @return {number}
 */

var countSubIslands = function(grid1, grid2) {
    const numRows = grid2.length;
    const numCols = grid2[0].length;
    const totalCells = numRows * numCols;
    const islandRoot = Array.from({ length: totalCells }, (_, i) => i);
    const islandStatus = new Uint8Array(totalCells);

    // Union islands in grid2
    for (let row = 0; row < numRows; row++) {
        for (let col = 0; col < numCols; col++) {
            if (grid2[row][col] === 1) {
                const currentIndex = row * numCols + col;
                if (col + 1 < numCols && grid2[row][col + 1] === 1) {
                    unionIslands(islandRoot, currentIndex, currentIndex + 1);
                }
                if (row + 1 < numRows && grid2[row + 1][col] === 1) {
                    unionIslands(islandRoot, currentIndex, currentIndex + numCols);
                }
            }
        }
    }

    // Mark invalid sub-islands
    for (let row = 0; row < numRows; row++) {
        for (let col = 0; col < numCols; col++) {
            if (grid2[row][col] === 1 && grid1[row][col] === 0) {
                const rootIndex = findIslandRoot(islandRoot, row * numCols + col);
                islandStatus[rootIndex] = 2; // Mark as invalid sub-island
            }
        }
    }

    // Count valid sub-islands
    let subIslandCount = 0;
    for (let row = 0; row < numRows; row++) {
        for (let col = 0; col < numCols; col++) {
            if (grid2[row][col] === 1) {
                const rootIndex = findIslandRoot(islandRoot, row * numCols + col);
                if (islandStatus[rootIndex] === 0) {
                    subIslandCount++;
                    islandStatus[rootIndex] = 1; // Mark as counted
                }
            }
        }
    }

    return subIslandCount;
};

function findIslandRoot(islandRoot, x) {
    if (islandRoot[x] !== x) {
        islandRoot[x] = findIslandRoot(islandRoot, islandRoot[x]); // Path compression
    }
    return islandRoot[x];
}

function unionIslands(islandRoot, x, y) {
    const rootX = findIslandRoot(islandRoot, x);
    const rootY = findIslandRoot(islandRoot, y);
    if (rootX !== rootY) {
        islandRoot[rootY] = rootX;
    }
}