var strangePrinter = function (s) {
    const n = s.length;
    const dp = Array.from({ length: n }, () => Array(n).fill(0));

    // Filling DP table
    for (let i = n - 1; i >= 0; i--) {
        dp[i][i] = 1; // A single character needs 1 turn
        for (let j = i + 1; j < n; j++) {
            dp[i][j] = dp[i][j - 1] + 1; // Initial assumption, print s[j] separately
            for (let k = i; k < j; k++) {
                if (s[k] === s[j]) {
                    dp[i][j] = Math.min(dp[i][j], dp[i][k] + dp[k + 1][j - 1]);
                }
            }
        }
    }

    return dp[0][n - 1];
};
