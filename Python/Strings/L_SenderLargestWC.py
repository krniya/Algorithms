def largestWordCount(messages, senders):
        msgCnt = {}
        for m,s in zip(messages, senders):
            if s not in msgCnt:
                msgCnt[s] = len(m.split())
            else:
                msgCnt[s] += len(m.split())
        m = max(msgCnt.values())
        l = []
        for k,v in msgCnt.items():
            if v==m:
                l.append(k)
        l.sort()
        return l[-1]


print(largestWordCount(["How is leetcode for everyone","Leetcode is useful for practice"],["Bob","Charlie"]))