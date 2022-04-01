def floodFill(image, sr, sc, newColor):
    cc = image[sr][sc]
    visited=[[False] * (len(image[0])) for _ in range(len(image))]
    toVisit = [[sr,sc]]
    while len(toVisit):
        currNode = toVisit.pop()
        i = currNode[0]
        j = currNode[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        image[i][j] = newColor
        if i > 0 and image[i-1][j] == cc and not visited[i-1][j]:
           toVisit.append([i-1,j])
        if i < len(image) - 1 and image[i+1][j] == cc and not visited[i+1][j]:
            toVisit.append([i+1,j])
        if j > 0 and image[i][j-1] == cc and not visited[i][j-1]:
            toVisit.append([i,j-1])
        if j < len(image[0]) - 1 and image[i][j+1] == cc and not visited[i][j+1]:
            toVisit.append([i,j+1])
    return image

def floodFill(image, sr, sc, newColor):
    R, C = len(image), len(image[0])
    color = image[sr][sc]
    if color == newColor: return image
    def dfs(r, c):
        if image[r][c] == color:
            image[r][c] = newColor
            if r >= 1: dfs(r-1, c)
            if r+1 < R: dfs(r+1, c)
            if c >= 1: dfs(r, c-1)
            if c+1 < C: dfs(r, c+1)
    dfs(sr, sc)
    return image