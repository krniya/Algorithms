
def calcEquation1(equations, values, queries):
        def answer(current, end, scalar):
            if current==end: return scalar
            visited.add(current)
            if current in graph:
                for i in graph[current]:
                    if i[0] not in visited:
                        a=answer(i[0],end,scalar*i[1])
                        if a!=-1: return a
            return -1

        graph={}
        for i in range(len(equations)):
            if equations[i][0] not in graph:
                graph[equations[i][0]]=[]
            if equations[i][1] not in graph:
                graph[equations[i][1]]=[]
            graph[equations[i][0]].append((equations[i][1],1/values[i]))
            graph[equations[i][1]].append((equations[i][0],values[i]))
        v=[]
        for i in queries:
            visited=set()
            if i[0] not in graph or i[1] not in graph:
                v.append(-1)
                continue
            v.append(1/answer(i[0],i[1],1) if i[0]!=i[1] else 1)
        return v


def calcEquation(eq, val, queries):
    graph = {}
    for (x,y), v in zip(eq, val):
        if x not in graph:
            graph[x] = {}
        if y not in graph:
            graph[y] = {}
        graph[x][y] = v
        graph[y][x] = 1.0 / v

    def dfs(x,y):
        if x not in graph or y not in graph:
            return -1
        if y in graph[x]:
            return graph[x][y]
        for i in graph[x]:
            if i not in visit:
                visit.add(i)
                t = dfs(i,y)
                if t == -1:
                    continue
                else:
                    return t * graph[x][i]
        return -1

    res = []
    for q in queries:
        visit = set()
        res.append(dfs(q[0],q[1]))
    return res



print(calcEquation([["a","b"],["b","c"]],
                    [2.0,3.0],
                    [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))