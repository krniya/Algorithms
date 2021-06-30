def jumpGame(nums):
    if len(nums) <= 1:
        return 0
    l, r = 0, nums[0]
    times = 1
    while r < len(nums) - 1:
        times += 1
        nxt = max(i + nums[i] for i in range(l, r + 1))
        l, r = r, nxt
    return times


def jumpGame1(nums):
    size = len(nums)
    destination = size - 1
    cur_coverage, last_jump_index = 0, 0
    times_of_jump = 0
    if size == 1:
        return 0
    for i in range(0, size):
        cur_coverage = max(cur_coverage, i + nums[i])
        if i == last_jump_index:
            last_jump_index = cur_coverage
            times_of_jump += 1
            if cur_coverage >= destination:
                return times_of_jump
    return times_of_jump


print(jumpGame1([2, 4, 1, 1, 4, 7, 1, 1, 3]))
