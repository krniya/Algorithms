def searchRange(nums, target):
        def bsearch(a,t,d):
            i,j=0,len(a)-1
            while i<=j:
                m=(i+j)//2
                if a[m] < t:
                    i = m+1
                else:
                    j=m-1
            return i if d=="l" else j
        l = bsearch(nums, target, "l")
        r = bsearch(nums, target, "r")
        return [l,r] if l<=r else [-1,-1]

print(searchRange([5,7,7,8,8,10], 8))