def alternateDigitSum(n: int) -> int:
        s=str(n)
        ans=0
        for i in range(0,len(s),2):
            ans+=int(s[i])
        for i in range(1,len(s),2):
            ans-=int(s[i])
        return ans