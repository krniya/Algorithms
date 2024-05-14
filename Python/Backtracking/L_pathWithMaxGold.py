class Solution:
    def __init__(self):
        self.maxGold = 0
        self.roww = [1, -1, 0, 0]
        self.coll = [0, 0, -1, 1]

    def checkIfAllNonZeros(self, grid):
        count = 0
        for row in grid:
            for cell in row:
                if cell != 0:
                    count += cell
                else:
                    return 0
        return count

    def backtrack(self, grid, x, y, count):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return

        if grid[x][y] != 0:
            curr = grid[x][y]
            grid[x][y] = 0
            count += curr
            self.maxGold = max(self.maxGold, count)

            for i in range(4):
                newX = x + self.roww[i]
                newY = y + self.coll[i]
                self.backtrack(grid, newX, newY, count)

            grid[x][y] = curr

    def getMaximumGold(self, grid):
        count = self.checkIfAllNonZeros(grid)
        if count != 0:
            return count

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    self.backtrack(grid, i, j, 0)

        return self.maxGold