def subarraySum(nums, k: int) -> int:
        res, prefSum, prefData= 0, 0, {0:1}
        for num in nums:
            prefSum = prefSum + num
            if prefSum-k in prefData:
                res = res + prefData[prefSum-k]
            prefData[prefSum] = prefData.get(prefSum,0) + 1
        return res

print(subarraySum([1,2,3], 3))