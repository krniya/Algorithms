def maxConsecutive(arr):
    nums = set(arr)
    best = 0
    for x in nums:
        if x - 1 not in nums:
            y = x + 1
            while y in nums:
                y += 1
            best = max(best, y - x)
    return best

print(maxConsecutive([8, 9, 1, 2, 3, 1]))