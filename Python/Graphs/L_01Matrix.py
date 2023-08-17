from collections import deque


def updateMatrix(matrix):
    visited = set()

    q = deque()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                visited.add((i,j))
                q.append((i,j))
        
    while q:
        x,y = q.popleft()
        for dirr in [(1,0), (-1,0), (0,1), (0,-1)]:
            newX, newY = x+dirr[0], y+dirr[1]
            if newX >= 0 and newX <= len(matrix)-1 and newY >= 0 and newY <= len(matrix[0])-1 and (newX, newY) not in visited:
                matrix[newX][newY] = matrix[x][y] + 1
                visited.add((newX, newY))
                q.append((newX, newY))
    return matrix


def updateMatrix1(mat):
        m, n = len(mat), len(mat[0])
        DIR = [0, 1, 0, -1, 0]

        q = deque([])
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = -1  # Marked as not processed yet!

        while q:
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i + 1]
                if nr < 0 or nr == m or nc < 0 or nc == n or mat[nr][nc] != -1: continue
                mat[nr][nc] = mat[r][c] + 1
                q.append((nr, nc))
        return mat

print(updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))