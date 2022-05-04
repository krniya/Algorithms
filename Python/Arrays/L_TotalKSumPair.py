from collections import defaultdict


def maxOperations(nums, k) -> int:
        nums.sort()
        c,l,r = 0,0,len(nums) - 1
        while l<r:
            curr = nums[l] + nums[r]
            if curr > k:
                r-=1
            elif curr < k:
                l+=1
            else:
                l+=1
                r-=1
                c+=1
        return c

def maxOperations(nums, k) -> int:
        ans = 0
        seen = defaultdict(int)
        for b in nums:
            a = k - b # Explain: a + b = k  =>  a = k - b
            if seen[a] > 0:
                ans += 1
                seen[a] -= 1
            else:
                seen[b] += 1
        return ans