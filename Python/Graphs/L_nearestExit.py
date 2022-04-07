def nearestExit(maze, entrance):
    row = len(maze)
    col = len(maze[0])
    er, ec = entrance
    maze[er][ec] = "+"
    q = [(er,ec,0)]
    while len(q):
        i,j,c = q.pop(0)
        if (i in [0,row-1] or j in [0,col-1]) and (er,ec) != (i,j):
            return c
        for x, y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            if 0 <= x <row and 0 <= y <col and maze[x][y] == ".":
                maze[x][y] = "+"
                q.append((x,y,c+1))
    return -1

print(nearestExit([["+",".","+","+","+","+","+"],
                   ["+",".","+",".",".",".","+"],
                   ["+",".","+",".","+",".","+"],
                   ["+",".",".",".","+",".","+"],
                   ["+","+","+","+","+","+","."]],
                   [0,1]))