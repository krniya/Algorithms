from functools import lru_cache


def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def counter(start, last, last_count, left): #count the cost of compressing from the start
            if left < 0:
                return float('inf') # this is impossible
            if start >= len(s):
                return 0
            if s[start] == last:
				# we have a stretch of the last_count of the same chars, what is the cost of adding one more? 
                incr = 1 if last_count == 1 or last_count == 9 or last_count == 99 else 0
				# no need to delete here, if we have a stretch of chars like 'aaaaa' - we delete it from the beginning in the else delete section
                return incr + counter(start+1, last, last_count+1, left) # we keep this char for compression
            else:
				# keep this char for compression - it will increase the result length by 1 plus the cost of compressing the rest of the string 
                keep_counter = 1 + counter(start+1, s[start], 1, left)
				# delete this char
                del_counter =  counter(start + 1, last, last_count, left - 1)
                return min(keep_counter, del_counter)
        return counter(0, "", 0, k)
    
    
def getLengthOfOptimalCompression(s: str, k: int) -> int:
    n = len(s)
    dp = [[9999] * 110 for _ in range(110)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(0, k + 1):
            cnt, del_ = 0, 0
            for l in range(i, 0, -1):
                if s[l - 1] == s[i - 1]:
                    cnt += 1
                else:
                    del_ += 1

                if j - del_ >= 0:
                    dp[i][j] = min(dp[i][j], dp[l - 1][j - del_] + 1 + (3 if cnt >= 100 else 2 if cnt >= 10 else 1 if cnt >= 2 else 0))

            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])

    return dp[n][k]