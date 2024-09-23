var minExtraChar = function (s, dictionary) {
    let dict = new Set(dictionary); // Store dictionary in a set for O(1) lookup
    let n = s.length;
    let dp = new Array(n + 1).fill(n); // DP array initialized with maximum extra characters
    dp[0] = 0; // No extra characters for an empty string

    // Iterate through the string
    for (let i = 1; i <= n; i++) {
        // Try all substrings ending at i
        for (let j = 0; j < i; j++) {
            let sub = s.substring(j, i); // Get substring s[j:i]
            if (dict.has(sub)) {
                dp[i] = Math.min(dp[i], dp[j]); // If substring found in dictionary
            }
        }
        dp[i] = Math.min(dp[i], dp[i - 1] + 1); // Consider current character as extra
    }

    return dp[n]; // Return the result from dp[n]
};
