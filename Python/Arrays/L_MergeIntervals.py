intervals = [[1,4], [3,5], [6,7], [2,3]]

def merge(intervals):
    out = []
    for i in sorted(intervals, key=lambda i: i[0]):
        if out and i[0] <= out[-1][-1]:
            out[-1][-1] = max(out[-1][-1], i[-1])
        else:
            out += i,
    return out

def merge1(intervals):
    intervals = sorted(intervals, key = lambda x: x[0])
    i = 0
    while i < len(intervals) - 1:
        if intervals[i][-1] >= intervals[i+1][0]:
            intervals[i][-1] = max(intervals[i][-1], intervals[i+1][-1])
            del intervals[i+1]
        else:
            i += 1
    return intervals

print(merge(intervals))