def minMoves2(nums) -> int:
        midVal = sorted(nums)[len(nums) // 2]
        res = 0
        for n in nums:
            res += abs(midVal - n)
        return res