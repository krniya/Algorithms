from collections import defaultdict
from tkinter import W


def largestWordCount(messages, senders) -> str:
        hm = defaultdict()
        n = len(messages)
        def split(s):
            w= 1
            for c in s:
                w+= c ==""
            return w
        for i in range(n):
            hm[senders[i]]= [split(messages[i])]
        res = ""
        cnt = 0
        for k in hm:
            if k>=cnt:
                cnt=k
                res = max(res,hm[k])
        return res

print(largestWordCount(["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"],["Alice","userTwo","userThree","Alice"]))