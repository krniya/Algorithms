def findCircleNum(isConnected):
    seen = set([])
    res = 0
    for i in range(len(isConnected)):
        if i not in seen:
            toSee = [i]
            while len(toSee):
                cur = toSee.pop()
                if cur not in seen:
                    seen.add(cur)
                    toSee = [j for j,v in enumerate(isConnected[cur]) if v and j not in seen] + toSee
            res += 1
    return res