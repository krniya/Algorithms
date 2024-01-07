def numberOfArithmeticSlices(nums) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        
        ans = 0
        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                cnt = 0
                if diff in dp[j]:
                    cnt = dp[j][diff]
                    
                dp[i][diff] += cnt + 1
                ans += cnt
                
        return ans
    
    
    
    
    
def numberOfArithmeticSlices1(nums):
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    map = {}

    for i in range(n):
        temp = nums[i]
        if temp not in map:
            map[temp] = []
        map[temp].append(i)

    total_sum = 0
    for i in range(1, n):
        for j in range(i + 1, n):
            a = 2 * nums[i] - nums[j]
            if a in map:
                for k in map[a]:
                    if k < i:
                        dp[i][j] += dp[k][i] + 1
                    else:
                        break
            total_sum += dp[i][j]

    return total_sum