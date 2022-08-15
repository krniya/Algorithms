def findOrder(numCourses: int, prerequisites):
        coursePrereq = { i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            coursePrereq[course].append(prereq)
        visited, cycle = set(), set()
        result = []
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for prereq in coursePrereq[crs]:
                if not dfs(prereq):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            result.append(crs)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []
        return result