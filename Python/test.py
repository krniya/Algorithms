def numIslands(grid) -> int:
    count = 0
    visited = [[False for value in row] for row in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if visited[i][j]:
                continue
            nodeToExp= [[i,j]]
            currSize = 0
            while len(nodeToExp):
                curr = nodeToExp.pop()
                a= curr[0]
                b= curr[1]
                if visited[a][b]:
                    continue
                visited[a][b] = True
                if grid[a][b] == "0":
                    continue
                currSize += 1
                unvisited = []
                if a > 0 and not visited[a-1][b]:
                    unvisited.append([a-1,b])
                if a < len(grid) - 1 and not visited[a+1][b]:
                    unvisited.append([a+1,b])
                if b > 0 and not visited[a][b-1]:
                    unvisited.append([a,b-1])
                if b < len(grid[0])-1 and not visited[a][b+1]:
                    unvisited.append([a,b+1])
                for unvisi in unvisited:
                    nodeToExp.append(unvisi)
            if currSize > 0:
                count+=1
        return count

print(numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))