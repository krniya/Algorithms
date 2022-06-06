def pacificAtlantic(heights):
        rows, cols = len(heights), len(heights[0])
        atl, pas, res = set(), set() , []
        def dfs(r,c,visit, prevHeight):
            if (r,c) in visit or r < 0 or c < 0 or r == rows or c == cols or prevHeight > heights[r][c]:
                return
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
            
        for r in range(rows):
            dfs(r,0,pas,heights[r][0])
            dfs(r,cols-1,atl,heights[r][cols-1])
        
        for c in range(cols):
            dfs(0,c,pas,heights[0][c])
            dfs(rows-1,c,atl,heights[rows-1][c])
            
        for r in range(rows):
            for c in range(cols):
                if (r,c) in atl and (r,c) in pas:
                    res.append([r,c])
        return res

def pacificAtlantic(matrix):
        if not matrix:
            return []
        p_visited = set()
        a_visited = set()
        rows, cols = len(matrix), len(matrix[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        def traverse(i, j, visited):
            if (i, j) in visited:
                return
            visited.add((i, j))
            # Traverse neighbors.
            for direction in directions:
                next_i, next_j = i + direction[0], j + direction[1]
                if 0 <= next_i < rows and 0 <= next_j < cols:
                    if matrix[next_i][next_j] >= matrix[i][j]:
                        traverse(next_i, next_j, visited)
        for row in range(rows):
            traverse(row, 0, p_visited)
            traverse(row, cols - 1, a_visited)
        for col in range(cols):
            traverse(0, col, p_visited)
            traverse(rows - 1, col, a_visited)
        return list(p_visited & a_visited)

print(pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))