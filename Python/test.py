def hasValidPath(grid) -> bool:
        if grid[0][0] == ")" or grid[-1][-1] == "(":
            return False
        m,n = len(grid) - 1, len(grid[0]) - 1
        if (m + n) % 2 == 0:
            return False
        def dfs(st, i, j):
            if not st and (i > m or j > n):
                return True
            if i > m or j > n:
                return False
            if grid[i][j] == "(":
                st.append(grid[i][j])
            elif grid[i][j] == ")":
                if not st:
                    return False
                st.pop()
            return dfs(st,i+1,j) or dfs(st,i,j+1)

        return dfs([],0,0)

print(hasValidPath([["(",")","("],[")",")",")"],["(","(",")"],["(","(",")"]]))
