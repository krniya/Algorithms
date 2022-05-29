def totalSteps(A) -> int:    
        st = [[A[0], 0]]
        ans = 0
        for a in A[1:]:
            t = 0
            while st and st[-1][0] <= a:
                t = max(t, st[-1][1])
                st.pop()
            if st: 
                t += 1
            else:
                t = 0
            ans = max(ans, t)
            st.append([a, t])
            
        return ans

print(totalSteps([5,3,4,4,7,3,6,11,8,5,11]))