def maximumBags(capacity, rocks, ar) -> int:
        cap = len(capacity)
        res=0
        for i in range(cap):
            capacity[i]-=rocks[i]
        capacity.sort()
        for i in range(cap):
            if ar < capacity[i]:
                break
            res+=1
            ar-=capacity[i]
        return res