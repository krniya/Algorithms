from typing import List

def findSubsequences(nums: List[int]) -> List[List[int]]:
        # Use set to store different subsequences to avoid duplicates
        res = set()
        
        def BT(i,subsequence):
            nonlocal res
            
            # As long as there are at least two elements, we add it to our result.
            # Note that the subsequence is non-decreasing since we checked it while building.
            if len(subsequence)>1:
                res.add(tuple(subsequence))
            
            # There are no more elements left to pick (no more state to generate), just return.
            if i==len(nums):
                return
            
            # Check to make sure the subsequence is non-decreasing if we want to pick the current element. 
            if not subsequence or nums[i] >= subsequence[-1]:
                                                    # Note that this line is the same as:
                                                    # subsequence.append(nums[i])   #change the current state to its neighboring state
                BT(i+1, subsequence+[nums[i]])      # BT(i+1, subsequence)          #backtrack(state)
                                                    # subsequence.pop()             #restore the state (backtrack)
            # Do not pick the current element.
            BT(i+1, subsequence)
        
        BT(0,[])
        return res