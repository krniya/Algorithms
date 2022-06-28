def minDeletions(s: str) -> int:
        cnt, res, used = {}, 0, set()
        for ch in s:
            cnt[ch] = cnt.get(ch,0) + 1
        for ch, freq in cnt.items():
            while freq > 0 and freq in used:
                freq -= 1
                res += 1
            used.add(freq)
        return res