def missingNumber(nums) -> int:
        a = len(nums)
        for i,n in enumerate(nums):
            a ^= i ^ n
        return a

print(missingNumber())