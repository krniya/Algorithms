def uncommonFromSentences(s1: str, s2: str):
        s1_count = {}
        s2_count = {}
        res = []
        for word in s1.split(" "):
            s1_count[word] = s1_count.get(word, 0) + 1
        for word in s2.split(" "):
            s2_count[word] = s2_count.get(word, 0) + 1
        for key, val in s1_count.items():
            if val == 1 and key not in s2_count:
                res.append(key)
        for key, val in s2_count.items():
            if val == 1 and key not in s1_count:
                res.append(key)
        return res
