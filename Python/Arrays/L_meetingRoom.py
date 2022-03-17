def cantAttendMeeting(intervals):
    intervals.sort(key= lambda x:x[0])
    for i in range(1, len(intervals)):
        i1 = intervals[i-1][1]
        i2 = intervals[i][0]
        if i1 > i2:
            return False
    return True

