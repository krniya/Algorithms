# O(wh) | O(wh)
def riverSize(matrix):
    sizes = []
    visited = [[False for value in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverseNode(i,j,matrix,visited,sizes)
    return sizes

def traverseNode(i,j,matrix,visited,sizes):
    currentSize = 0
    nodetoExplore = [[i, j]]
    while len(nodetoExplore):
        currentNode = nodetoExplore.pop()
        i = currentNode[0]
        j = currentNode[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        currentSize += 1
        unvisitedNeighbour = getUnvisitedNeighbour(i,j,matrix,visited)
        for neighbour in unvisitedNeighbour:
            nodetoExplore.append(neighbour)
    if currentSize > 0:
        sizes.append(currentSize)
        
def getUnvisitedNeighbour(i,j,matrix,visited):
    unvisitedNeighbour = []
    if i>0 and not visited[i-1][j]:
        unvisitedNeighbour.append([i-1, j])
    if i<len(matrix) - 1 and not visited[i + 1][j]:
        unvisitedNeighbour.append([i+1, j])
    if j>0 and not visited[i][j-1]:
        unvisitedNeighbour.append([i,j-1])
    if j<len(matrix[0]) - 1 and not visited[i][j+1]:
        unvisitedNeighbour.append([i,j+1])
    return unvisitedNeighbour

print(riverSize([[1,0,1,1,0],
                 [1,0,0,1,1],
                 [0,1,1,0,0],
                 [1,0,0,1,1]]))
