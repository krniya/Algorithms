def maxScore(cardPoints, k: int) -> int:
        s = sum(cardPoints[:k])
        res = s
        for i in range(1, k+1):
            s += cardPoints[-i] - cardPoints[k-i]
            res = max(res, s)
        return res

print(maxScore([1,2,3,4,5,6,1], 3))