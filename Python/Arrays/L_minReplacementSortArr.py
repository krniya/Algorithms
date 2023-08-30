from math import ceil


def minimumReplacement(nums):
    n = len(nums)
    ret = 0
    prev = nums[n - 1]
    for ind in range(n - 2, -1, -1):
        num = nums[ind]
        k = ceil(num / prev)
        ret += k - 1
        prev = num // k
    return ret
