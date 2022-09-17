def palindromePairs(words):
        palins = set()
        
        def isPalindrome(s):
            if s == s[::-1]:
                palins.add(s)
                return True
            return False

        mem = {word: i for i, word in enumerate(words)}
        res = []
        
        
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                pref = word[:j]
                suff = word[j:]
                        
                if pref in palins or isPalindrome(pref):
                    rev = suff[::-1]
                    if rev in mem and i != mem[rev]:
                        res.append((mem[rev], i))
                        
                if suff and (suff in palins or isPalindrome(suff)):
                    rev = pref[::-1]
                    if rev in mem and i != mem[rev]:
                        res.append((i, mem[rev]))

        return res