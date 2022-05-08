def largestGoodInteger(num: str) -> str:
        res = '' 
        cnt = 1
        for i in range(1, len(num)):
            if num[i] == num[i-1]:
                cnt+=1
            else:
                cnt = 1
            if cnt == 3:
                res = max(res, num[i] * 3)
                
        return res