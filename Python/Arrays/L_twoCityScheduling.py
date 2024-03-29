def twoCitySchedCost(costs):
    diffs = []
    for c1, c2 in costs:
        diffs.append([c2-c1,c1,c2])
    ans = 0
    diffs.sort()
    for i in range(len(diffs)):
        if i < len(diffs) // 2:
            ans += diffs[i][2]
        else:
            ans += diffs[i][1]
    return ans