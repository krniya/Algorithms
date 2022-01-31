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