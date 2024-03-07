#include <bits/stdc++.h>
using namespace std;

int bagOfTokensScore(vector<int> &tokens, int power)
{
    sort(tokens.begin(), tokens.end()); // sort the token
    int s = 0;                          // Initialize the Score
    int maxi = 0;                       // Track the maximum score
    int l = 0, r = tokens.size() - 1;   // Left and Right pointer
    while (l <= r)
    {
        if (power >= tokens[l])
        {                        // If the remaining power is greater than or equal to the smallest token
            power -= tokens[l];  // Reduce the Power
            s++;                 // Increase the score
            l++;                 // Move the left pointer to the right.
            maxi = max(maxi, s); // Update the maximum score if the current score is higher.score
        }
        else if (s > 0)
        {                       // If the current score is positive, consider trading tokens for power.
            power += tokens[r]; // increase the power
            s--;                // Decrease the score.
            r--;                // Move the right pointer to the left.
        }
        else
        {
            break; // exit the loop if neither condition is met
        }
    }

    return maxi;
}