def longestConsecutive(nums) -> int:
        res = 0
        nums = set(nums)
        for num in nums:
            if num - 1 not in nums:
                left = num
                right = num
                while right + 1 in nums:
                    right += 1
                res = max(res, right - left + 1)
        return res

def longestConsecutive(nums) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            if n-1 not in numSet:
                num = n + 1
                while num in numSet:
                    num += 1
                longest = max(longest, num - n)
        return longest