from collections import defaultdict


def maximumSum(nums) -> int:
        def digitSum(n):
            res = 0
            while n:
                res += n % 10
                n //= 10
            return res
        dSum = defaultdict(list)
        res = -1
        for num in nums:
            dSum[digitSum(num)].append(num)
        for val in dSum.values():
            if len(val) > 1:
                val.sort()
                res = max(res, val[-1] + val[-2])
        return res