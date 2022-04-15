from collections import defaultdict


def numOfMinutes1(n, headID, manager, informTime):
        graph = defaultdict(list)
        for i in range(len(manager)):
            graph[manager[i]].append(i)
        
        def dfs(u):
            ans = 0
            for v in graph[u]:
                ans = max(dfs(v) + informTime[u], ans)
            return ans
        
        return dfs(headID)

def numOfMinutes(n, headID, manager, informTime):
        def dfs(ind):
            if manager[ind]!=-1:
                informTime[ind]+=dfs(manager[ind])
                manager[ind]=-1
            return informTime[ind]
        for i in range(n):
            dfs(i)
        return max(informTime)

print(numOfMinutes(6,2,[2,2,-1,2,2,2],[0,0,1,0,0,0]))