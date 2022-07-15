def minWindow1(s: str, t: str) -> str:
        if t == "":
            return ""
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        have, need = 0, len(countT)
        res, resLen = [-1,-1], float("inf")
        l=0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)
            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = (r-l+1)
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l+=1
        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""

def minWindow( s: str, t: str) -> str:
        if t == "":
            return t
        word, target = {}, {}
        left, size, res = 0, float("inf"), [-1,-1]
        for ch in t:
            target[ch] = target.get(ch,0) + 1
        need, have = len(target), 0
        for right, ch in enumerate(s):
            word[ch] = word.get(ch,0) + 1
            if ch in target and word[ch] == target[ch]:
                have += 1
            while have == need:
                if (right - left + 1) < size:
                    size = right - left + 1
                    res = [left, right]
                word[s[left]] -= 1
                if s[left] in target and target[s[left]] > word[s[left]]:
                    have -= 1
                left += 1
        return s[res[0]:res[1]+1]

print(minWindow("aa", "aa"))
            
