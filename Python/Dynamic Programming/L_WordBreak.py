def word_break(s, words):
    d = [False] * len(s)    
    for i in range(len(s)):
        for w in words:
            temp = s[i-len(w)+1:i+1]
            if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                d[i] = True
    return d[-1]

print (word_break("leetcode", ["leet", "code"]))
# print (word_break("catsandog", ["cats","dog","sand","and","cat"]))

