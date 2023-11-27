def knightDialer(n: int) -> int:
    if n == 1:
        return 10
    jump = [
        [4,6],
        [8,6],
        [7,9],
        [4,8],
        [3,9,0],
        [],
        [1,7,0],
        [2,6],
        [1,3],
        [2,4]           
    ]
    dp = [1] * 10
    MOD = 10 ** 9 + 7
    for _ in range(n-1):
        next_dp = [0] * 10
        for n in range(10):
            for d in jump[n]:
                next_dp[d] =(next_dp[d] + dp[n])
        dp = next_dp
    return sum(dp) % MOD