class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        if current == correct:
            return 0
        current = current.split(":")
        correct = correct.split(":")
        res = 0
        if int(correct[0]) > int(current[0]):
            res += abs(int(correct[0]) - int(current[0]))
        elif int(correct[0]) == int(current[0]) and int(correct[1]) < int(current[1]):
            res+= 23
        elif int(correct[0]) == int(current[0]) and int(correct[1]) > int(current[1]):
            res+= 0
        else:
            res += 24 - abs(int(correct[0]) - int(current[0]))
        if int(correct[1]) >= int(current[1]):
            diff = int(correct[1]) - int(current[1])
            while diff >= 15:
                diff -= 15
                res+= 1
            while diff >= 5:
                diff -= 5
                res+=1
            res += diff
        else:
            res -= 1
            diff = 60 - abs(int(correct[1]) - int(current[1]))
            while diff >= 15:
                diff -= 15
                res+= 1
            while diff >= 5:
                diff -= 5
                res+=1
            res += diff     
        return res


def convertTime(current, correct):
    def f(x):
        a, b = map(int, x.split(':'))
        return a*60+b
    s = f(correct)-f(current)
    ans = 0
    for i in [60, 15, 5, 1]:
        x = s//i
        s %= i
        ans += x
    return ans