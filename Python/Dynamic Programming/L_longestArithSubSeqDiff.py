from typing import List


def longestSubsequence(arr: List[int], difference: int) -> int:
        n = len(arr)
        dp = [1] * n
        for i in range(n-2, -1, -1):
            for j in range(i, n):
                if arr[j] - arr[i] == difference:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
    
def longestSubsequence(arr: List[int], difference: int) -> int:
        n = len(arr)
        dp = {}  # Stores the maximum length at each index
        ans = 1  # Initialize with the minimum length of 1
        for i in range(n):
            num = arr[i]
            if num - difference in dp:
                dp[num] = dp[num - difference] + 1
            else:
                dp[num] = 1
            ans = max(ans, dp[num])
        return ans
    
print(longestSubsequence([9,-9,-12,-12,8,8], 0))