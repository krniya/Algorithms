from collections import defaultdict
from itertools import combinations


def maxProduct(words):
        d, ans = defaultdict(int), 0
        for word in words:
            for l in word:
                d[word] |= 1<<(ord(l) - 97)
                
        for w1, w2 in combinations(d.keys(), 2):
            if d[w1] & d[w2] == 0: 
                ans = max(ans, len(w1)*len(w2))
                
        return ans

print(maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))