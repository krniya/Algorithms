def maxScore(s: str) -> int:
    left = -1
    zeros = 0
    ones = 0

    for i in range(len(s) - 1):
        if s[i] == '0':
            zeros += 1
        else:
            ones += 1

        left = max(left, zeros - ones)
    
    ones += s[-1] == "1"

    return left + ones