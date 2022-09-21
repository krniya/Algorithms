def sumEvenAfterQueries(nums, queries):
        currSum = 0
        for num in nums:
            currSum += num if num % 2 == 0 else 0
        res = []
        for num, idx in queries:
            nSum = (nums[idx] + num)
            if nSum % 2 == 0:
                if nums[idx] % 2:
                    currSum += nSum
                else:
                    currSum += num
            else:
                if nums[idx] % 2 == 0:
                    currSum -= nums[idx]
            res.append(currSum)
            nums[idx] = nSum
        return res

print(sumEvenAfterQueries([1,2,3,4],[[1,0],[-3,1],[-4,0],[2,3]]))