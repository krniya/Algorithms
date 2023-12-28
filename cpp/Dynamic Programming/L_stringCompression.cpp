
#include <bits/stdc++.h>
using namespace std;

class Solution
{
    const static int N = 127;

    // dp[left][k] means the minimal coding size for substring
    // s[left:] and removing at most k chars
    int dp[N][N];

    string str;
    int n;

    // get length of digit
    inline int xs(int x) { return x == 1 ? 0 : x < 10 ? 1
                                           : x < 100  ? 2
                                                      : 3; }

    int solve(int left, int k)
    {
        if (k < 0)
            return N; // invalid, return INF
        if (left >= n or n - left <= k)
            return 0; // empty

        int &res = dp[left][k];
        if (res != -1)
            return res;
        res = N;

        int cnt[26] = {0};
        // we try to make s[left:j] (both inculded) as one group,
        // and all chars in this group should be the same.
        // so we must keep the most chars in this range and remove others
        // the range length is (j - left + 1)
        // and the number of chars we need to remove is (j - left + 1 - most)
        for (int j = left, most = 0; j < n; j++)
        {
            most = max(most, ++cnt[str[j] - 'a']); // most = max(count(s[left:j])
            res = min(res, 1 + xs(most) + solve(j + 1, k - (j - left + 1 - most)));
        }
        return res;
    }

public:
    int getLengthOfOptimalCompression(string s, int k)
    {
        memset(dp, -1, sizeof(dp));
        str = s;
        n = s.size();
        return solve(0, k);
    }
}

int
getLengthOfOptimalCompression(string s, int k)
{
    int n = s.length();
    vector<vector<int>> dp(110, vector<int>(110, 9999)); // Initializing a 2D vector 'dp' of size 110x110 with value 9999
    dp[0][0] = 0;                                        // Initializing the base case where no characters and deletions exist

    for (int i = 1; i <= n; i++)
    {
        for (int j = 0; j <= k; j++)
        {
            int cnt = 0, del = 0;
            for (int l = i; l >= 1; l--)
            {
                // Count the frequency of characters from 'i' to 'l'
                if (s[l - 1] == s[i - 1])
                    cnt++;
                else
                    del++;

                // Check if the remaining allowed deletions are valid (j - del >= 0)
                if (j - del >= 0)
                {
                    // Update the dp array based on the conditions
                    dp[i][j] = min(dp[i][j],
                                   dp[l - 1][j - del] + 1 + (cnt >= 100 ? 3 : cnt >= 10 ? 2
                                                                          : cnt >= 2    ? 1
                                                                                        : 0));
                }
            }

            // If there are remaining allowed deletions (j > 0), consider the case without deleting current character
            if (j > 0)
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1]);
        }
    }
    return dp[n][k]; // Return the minimum length for 's' with at most 'k' deletions
};