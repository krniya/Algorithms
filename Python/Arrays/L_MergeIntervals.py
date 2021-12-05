intervals = [[1,4], [3,5], [6,7], [2,3]]

def merge(intervals):
    out = []
    for i in sorted(intervals, key=lambda i: i[0]):
        if out and i[0] <= out[-1][-1]:
            out[-1][-1] = max(out[-1][-1], i[-1])
        else:
            out += i,
    return out

print(merge(intervals))