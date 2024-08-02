def minSwaps(nums) -> int:
    k = nums.count(1)
    mx = cnt = sum(nums[:k])
    n = len(nums)
    for i in range(k, n + k):
        cnt += nums[i % n]
        cnt -= nums[(i - k + n) % n]
        mx = max(mx, cnt)
    return k - mx