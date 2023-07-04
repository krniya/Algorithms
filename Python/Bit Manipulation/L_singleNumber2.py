def singleNumber(nums) -> int:
        o = t = 0
        for i in range(len(nums)):
            o = (o ^ nums[i]) & ~t
            t = (t ^ nums[i]) & ~o
        return o
    
    
def singleNumber(nums) -> int:
        hm = {}
        for n in nums:
            hm[n] = hm.get(n,0) + 1
        for k,v in hm.items():
            if v == 1:
                return k