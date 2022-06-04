def courseSchedule(numCourse, prerequisites):
    crsMap = { i:[] for i in range(numCourse)}
    for crs, pre in prerequisites:
        crsMap[crs].append(pre)
    visited = set()
    def dfs(crs):
        if crs in visited: return False
        if crsMap[crs] == []: return True
        visited.add(crs)
        for pre in crsMap[crs]:
            if not dfs(pre): return False
        visited.remove(crs)
        crsMap[crs] = []
        return True
    for crs in range(numCourse):
        if not dfs(crs): return False
    return True

def courseSchedule2(n, prerequisites):
        G = [[] for i in range(n)]
        degree = [0] * n
        for j, i in prerequisites:
            G[i].append(j)
            degree[j] += 1
        bfs = [i for i in range(n) if degree[i] == 0]
        for i in bfs:
            for j in G[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    bfs.append(j)
        return len(bfs) == n


print(courseSchedule2(3,[[0,1],[0,2],[1,2]]))