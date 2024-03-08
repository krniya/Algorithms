def maxFrequencyElements(nums) -> int:
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    max_num = max(count.values())
    max_count = list(count.values()).count(max_num)
    return max_num * max_count