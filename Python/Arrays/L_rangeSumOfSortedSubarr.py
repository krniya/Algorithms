def rangeSum(nums, n: int, left: int, right: int) -> int:
    all_sum = []
    for i in range(n):
        curr_sum = 0
        for j in range(i,n):
            curr_sum += nums[j]
            all_sum.append(curr_sum)
    all_sum.sort()
    return sum(all_sum[left-1:right])

print(rangeSum([1,2,3,4], 4, 1, 5))