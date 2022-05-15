def maximumWhiteTiles(T, clen) -> int:
        T.sort()
        pref = [0]
        for i,(l,r) in enumerate(T):
            pref.append(pref[i]+r-l+1)
        ends = [i[-1] for i in T]
        
        n = len(ends)
        j, ans = 0, 0
        
        for i in range(n):
            l = T[i][0]                       
            r = min(ends[-1], l + clen - 1)  

            while j < n and ends[j] < r:    
                j += 1

            if T[j][0] > r:   
                ans = max(ans, pref[j] - pref[i])
            else:              
                ans = max(ans, pref[j + 1] - pref[i] - ends[j] + r)
        return ans

print(maximumWhiteTiles([[1,5],[10,11],[12,18],[20,25],[30,32]], 10))