def removeCoveredIntervals(intervals):
    intervals.sort(key=lambda x:(x[0], -x[1]))
    res=[intervals[0]]
    for l,r in intervals[1:]:
        prevL, prevR = res[-1]
        if prevL <= l and prevR >= r:
            continue
        res.append([l,r])
    return len(res)

    

print(removeCoveredIntervals([[1,4],[3,6],[2,8]]))