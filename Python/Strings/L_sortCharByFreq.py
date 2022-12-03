def frequencySort(s: str) -> str:
        counter = {}
        for ch in s:
            counter[ch] = 1 + counter.get(ch, 0)
        res = ""
        for k in sorted(counter, key=counter.get, reverse=True):
            res += k * counter[k]
        return res