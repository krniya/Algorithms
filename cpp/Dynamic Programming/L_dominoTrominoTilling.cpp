#include<bits/stdc++.h>
using namespace std;

const int MOD = 1e9+7;
int numTilings(int n) {
    vector<vector<int>> dp(3, vector<int>(2));  // note only 3 rows are declared
    dp[1] = {1, 1}, dp[2] = {2, 2};
    for(int i = 3; i <= n; i++) {
        dp[i%3][0] = (dp[(i-1)%3][0] + dp[(i-2)%3][0] + 2l*dp[(i-2)%3][1]) % MOD;
        dp[i%3][1] = (dp[(i-1)%3][0] + dp[(i-1)%3][1]) % MOD;
    }
    return dp[n%3][0];
}


const int MOD = 1e9+7;
int dp[1001][2]{};
int numTilings(int n) {
    return solve(0, n, false);
}
long solve(int i, int n, bool previousGap) {
    if(i > n) return 0;
    if(i == n) return !previousGap;
    if(dp[i][previousGap]) return dp[i][previousGap];
    if(previousGap)
        return dp[i][previousGap] = (solve(i+1, n, false) + solve(i+1, n, true)) % MOD;
    return dp[i][previousGap] = (solve(i+1, n, false) + solve(i+2, n, false) + 2*solve(i+2, n, true)) % MOD;
}