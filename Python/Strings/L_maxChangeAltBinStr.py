def minOperations(s: str) -> int:
    op_count_odd = 0
    op_count_even = 0
    for i, ch in enumerate(s):
        if i % 2 == 0:
            if ch == '0':
                op_count_odd += 1
            else:
                op_count_even += 1
        else:
            if ch == '0':
                op_count_even += 1
            else:
                op_count_odd += 1
    return min(op_count_even, op_count_odd)
