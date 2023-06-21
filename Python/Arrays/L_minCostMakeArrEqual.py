from itertools import accumulate


def minCost(nums, cost) -> int:
        n = len(cost)
        ll = sorted([[nums[i], cost[i]] for i in range(n)])
        c_cumm_sum = list(accumulate([ll[i][1] for i in range(n)]))
        nc_cumm_sum = list(accumulate([ll[i][0] * ll[i][1] for i in range(n)]))
        res = float('inf')
        for i in range(n):
            res = min(res, ll[i][0] * (c_cumm_sum[i] - (c_cumm_sum[n-1] - c_cumm_sum[i]))
                         + (-(nc_cumm_sum[i]) + (nc_cumm_sum[n-1] - nc_cumm_sum[i])))
        return res