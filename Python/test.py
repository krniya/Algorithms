def longestPalin(s):
    longest = [0, 1]
    for i in range(1, len(s)):
        odd = getLongest(s, i-1, i+1)
        even = getLongest(s, i-1, i)
        maxP = max(odd, even, key=lambda x: x[1] - x[0])
        longest = max(longest, maxP, key=lambda x: x[1] - x[0])
        return s[longest[0]:longest[1]]


def getLongest(s, l, r):
    while l >= 0 and r < len(s):
        if s[l] != s[r]:
            break
        l -= 1
        r += 1
    return [l+1, r]


print(longestPalin("aaaabaa"))
