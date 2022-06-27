def countHousePlacements(n: int) -> int:
        if(n==1):return 4
        if(n==2):return 9
        
        MOD=10**9+7
        
        prev_prev=2
        prev=3
        for i in range(3,n+1):
            current=prev+prev_prev
            prev_prev=prev
            prev=current
            
        return (prev*prev)%MOD