
def tallestBillboard(rods) -> int:
    def dfs(i,left,right):
        if i==len(rods):
            return left if left == right else 0
        nleft = dfs(i+1, left + rods[i], right)
        nright = dfs(i+1, left, right + rods[i])
        nNone = dfs(i+1, left, right)
        return max(nleft, nright, nNone)
        
    return dfs(0,0,0)

def tallestBillboard(rods) -> int:
        dp = {0: 0} 
        # Iterate over each rod 
        for r in rods: 
            # Make a copy of dp, representing the cases where we don't add r to either stand 
            new_dp = dp.copy() 
            # For each diff and taller pair in dp 
            for diff, taller in dp.items(): 
                # Calculate the shorter height 
                shorter = taller - diff 
                # Add r to the taller stand, thus increasing the height difference to diff + r 
                new_dp[diff + r] = max(new_dp.get(diff + r, 0), taller + r) 
                # Add r to the shorter stand, thus resulting in a new height difference 
                # calculated as the absolute value of (shorter + r - taller) 
                new_diff = abs(shorter + r - taller) 
                new_taller = max(shorter + r, taller) 
                new_dp[new_diff] = max(new_dp.get(new_diff, 0), new_taller) 
            # Update dp to be the new_dp for the next iteration 
            dp = new_dp 
        # Return the maximum possible height of the billboard, which corresponds to a height difference of 0 
        return dp.get(0, 0)