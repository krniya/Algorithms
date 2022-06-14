def minDistance(word1: str, word2: str) -> int:
        w1 = len(word1)
        w2 = len(word2)
        dp = [[0] * (w2+1) for _ in range(w1+1)]
        for i in range(w2+1):
            dp[0][i] = i
        for i in range(w1+1):
            dp[i][0] = i
        for i in range(1,w1+1):
            for j in range(1,w2+1):
                if word1[i-1] != word2[j-1]:
                    dp[i][j] = min(dp[i][j-1],dp[i-1][j]) + 1
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]

print(minDistance("mart","karma"))