def findAndReplacePattern(words, pattern):
    res = []
    pat = converter(pattern)
    for word in words:
        if converter(word) == pat:
            res.append(word)
    return res

def converter(word):
    i=1
    res= {}
    op = []
    for ch in word:
        if ch in res:
            op.append(str(res[ch]))
        else:
            op.append(str(i))
            res[ch] = i
            i+=1
    return ",".join(op)

print(findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb"))