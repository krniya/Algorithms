def wordBreak(s, words):
    ok = [True]
    max_len = max(map(len,words+['']))
    words = set(words)
    for i in range(1, len(s)+1):
        ok += any(ok[j] and s[j:i] in words for j in range(max(0, i-max_len),i)),
    return ok[-1]

def word_break(s, words):
    d = [False] * len(s)
    temp=[]
    for i in range(len(s)):
        for w in words:
            temp.append(s[i-len(w)+1:i+1])
            if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                d[i] = True
    return d[-1]

print(word_break("leetcode", ["leet", "code"]))