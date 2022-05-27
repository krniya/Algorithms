def numberOfSteps(num: int) -> int:
        res = 0
        while num:
            if num % 2 ==  0:
                num>>=1
                res+=1
            else:
                num^=1
                res += 1
        return res

print(numberOfSteps(14))