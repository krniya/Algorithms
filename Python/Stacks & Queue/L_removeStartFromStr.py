def removeStars(s: str) -> str:
        ans=[]
        for i in s:
            if i=='*':
                ans.pop()
            else:
                ans+=[i]
        return "".join(ans)
