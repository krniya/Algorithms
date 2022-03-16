def solve(intervals):
    starts = sorted([interval[0] for interval in intervals])
    ends = sorted([interval[1] for interval in intervals])
    meet_count, cur_count = 0, 0
    s_ptr, e_ptr = 0, 0
    while s_ptr < len(intervals):
        if starts[s_ptr] < ends[e_ptr]:
            s_ptr += 1
            cur_count += 1
        else:
            e_ptr += 1
            cur_count -= 1
        meet_count = max(meet_count, cur_count)
    return meet_count

