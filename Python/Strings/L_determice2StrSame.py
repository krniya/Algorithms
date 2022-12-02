def closeStrings(word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        cnt1,cnt2 = {}, {}
        for ch in word1:
            cnt1[ch] = 1 + cnt1.get(ch, 0)
        for ch in word2:
            cnt2[ch] = 1 + cnt2.get(ch, 0)       
            
        res1 = [val for val in cnt1.values()]
        res2 = [val for val in cnt2.values()]
        res1.sort()
        res2.sort()
        return res1 == res2 and set(word1) == set(word2)