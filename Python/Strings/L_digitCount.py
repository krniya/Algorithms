from collections import defaultdict


def digitCount(num: str) -> bool:
        hm = defaultdict(lambda: 0)
        n = len(num)
        for n in num:
            if n not in hm:
                hm[n]=1
            else:
                hm[n]+=1
        for i,n in enumerate(num):
            if hm[str(i)] != int(n):
                return False
        return True