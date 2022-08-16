def noOfConnComp(n, edges):
    parent = [ i for i in range(n)]
    rank = [1] * n

    def find(n):
        par = parent[n]
        while par != parent[par]:
            parent[par] = parent[parent[par]]
            par = parent[par]
        return par

    def union(n1,n2):
        p1, p2 = find(n1), find(n2)
        if p1==p2:
            return 0
        if rank[n1] > rank[n2]:
            parent[n2] = n1
            rank[n1] += rank[n2]
        else:
            parent[n1] = n2
            rank[n2] += rank[n1]
        return 1

    res = n
    for n1, n2 in edges:
        res -= union(n1, n2)
    return res

print(noOfConnComp(6, [[0,1],[2,3],[3,5],[2,4]]))