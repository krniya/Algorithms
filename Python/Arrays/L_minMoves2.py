def minMoves2(nums):
    middle = sorted(nums)[len(nums) // 2]
    return sum(abs(num - middle) for num in nums)