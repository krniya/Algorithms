def answerQueries(a, q):
        a.sort()
        for i in range(1,len(a)): a[i]+= a[i-1]
        for i in range(0,len(q)): q[i]= Binary_Search(a,q[i])
        return q
        
    
def Binary_Search(a,val):
        start = 0
        end = len(a) - 1
        ans = -1
        while start <= end:
            mid = start + (end - start) // 2
            if a[mid] <= val:
                ans = mid
                start = mid + 1
            else:
                end = mid - 1
        return ans+1