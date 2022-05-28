from gettext import find


def findSubstring(s, words):
        if not s or not words or not words[0]:
            return []
        n = len(s)
        k = len(words[0])
        t = len(words) * k
        req = {}
        for w in words:
            req[w] = req[w] + 1 if w in req else 1
        ans = []
        def helper( l, r):
            curr = {}
            while r + k <= n:
                w = s[r:r + k]
                r += k
                if w not in req:
                    l = r
                    curr.clear()
                else:
                    curr[w] = curr[w] + 1 if w in curr else 1
                    while curr[w] > req[w]:
                        curr[s[l:l + k]] -= 1
                        l += k
                    if r - l == t:
                        ans.append(l)
        for i in range(min(k, n - t + 1)):
            helper(i, i)
        return ans

print(findSubstring("barfoothefoobarman", ["foo","bar"]))