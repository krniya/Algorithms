from collections import deque


def shortestPathAllKeys(grid) -> int:
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        totalKeys = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                curr = grid[i][j]
                if curr == "@":
                    x,y = i,j
                if "a" <= curr <= "f":
                    totalKeys += 1
        start = (0, x, y)
        queue = deque([start])
        visited = set()
        visited.add(start)
        steps = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                key, i, j = queue.popleft()
                if key == (1 << totalKeys) - 1:
                    return steps
                for x, y in directions:
                    ni, nj = i + x, j + y
                    newKey = key
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                        c = grid[ni][nj]
                        if c == "#":
                            continue
                        if "a" <= c <= "f":
                            newKey |= 1 << (ord(c) - ord("a"))
                        if "A" <= c <= "F" and not (key >> (ord(c) - ord("A")) & 1):
                            continue
                        if (newKey, ni, nj) not in visited:
                            visited.add((newKey, ni, nj))
                            queue.append((newKey, ni, nj))
            steps += 1
        return -1
        
        
print(shortestPathAllKeys((["@.a..","###.#","b.A.B"])))