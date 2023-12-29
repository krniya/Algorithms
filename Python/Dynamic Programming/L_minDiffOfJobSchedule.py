from functools import cache


def minDifficulty(jobDifficulty, d: int) -> int:
        n = len(jobDifficulty)
    
        @cache
        # dp(i, k): min difficulty when you start working on i-th job at day `k`
        def dp(i, k):
            # reach the last day
            # we put all the remaining jobs on this day
            # so we return the one with max difficulty
            if k == d: return max(jobDifficulty[i:])
            # init min difficulty with inf 
            res = float('inf')
            # cur is the max difficulty we've seen so far on day `k`
            # init current max with 0
            cur = 0
            # for jobDifficulty like 6 5 4 3 2 1, 
            # we can have following ways to distribute them into two days
            # 6 | 5 4 3 2 1
            # 6 5 | 4 3 2 1 
            # 6 5 4 | 3 2 1
            # 6 5 4 3 | 2 1
            # 6 5 4 3 2 | 1
            # notice that each day we must have at least one task
            # given the starting index `i`, 
            # we can only at most choose the jobs till the position `n - d + k - 1`
            for j in range(i, n - d + k):
                cur = max(cur, jobDifficulty[j])
                # if j-th job is the last job on day `k`, 
                # the max difficulty for day `k` is `cur`
                # and we need to start (j + 1)-th job on the next day
                # the result would be `cur + dp(j + 1, k + 1)`
                # then we take the min
                res = min(res, cur + dp(j + 1, k + 1))
            return res
        # n < d : you will have free days. hence you cannot find a schedule for the given jobs
        # e.g. Example 2
        # otherwise, we start working on 0-th job at day 1
        return -1 if n < d else dp(0, 1)
    
    
def minDifficulty(jobDifficulty, d):
        if len(jobDifficulty) < d:
            return -1
        total_sum = sum(jobDifficulty)
        if total_sum == 0:
            return 0
        return self.helper(jobDifficulty, d, 0)

def helper(jd, daysLeft, idx):
    length = len(jd)
    if daysLeft == 1:
        return max(jd[idx:])
    
    max_difficulty = jd[idx]
    daysLeft -= 1
    stop = length - idx - daysLeft + 1

    result = float('inf')
    for i in range(1, stop):
        max_difficulty = max(max_difficulty, jd[idx + i - 1])
        other = self.helper(jd, daysLeft, idx + i)
        result = min(result, other + max_difficulty)
    return result