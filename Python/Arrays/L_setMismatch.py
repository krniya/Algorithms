def findErrorNums(nums):
        s = len(nums)*(len(nums)+1) // 2
        a = sum(nums)
        u = sum(set(nums))
        return [a-u,s-u]