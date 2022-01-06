def longestCommonPrefix(m):
    if not m: return ''
    s1 = min(m)
    s2 = max(m)
    for i, c in enumerate(s1):
        if c != s2[i]:
            return s1[:i] #stop until hit the split index
    return s1


print(longestCommonPrefix(["apples", "apy", "aaam"]))