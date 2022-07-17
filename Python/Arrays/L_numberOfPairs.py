def numberOfPairs(nums):
        count = {}
        res = [0,0]
        for num in nums:
            count[num] = count.get(num,0) + 1
        for val in count.values():
            res[0] += val // 2
            res[1] += val %  2
        return res