def minMeetingRoom(intervals):
    start = sorted([i[0] for i in intervals])
    end = sorted([i[1] for i in intervals])
    i = j = res = count = 0
    while i < len(start):
        if start[i] < end[j]:
            count += 1
            i += 1
        else:
            count -= 1
            j += 1
        res = max(res, count)
    return res
