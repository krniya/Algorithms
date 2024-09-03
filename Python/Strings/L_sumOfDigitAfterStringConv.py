def getLucky(s: str, k: int) -> int:
        ns = ""
        for ch in s:
            ns += str(ord(ch) - ord('a')+1)
        while k:
            total = 0
            for ch in ns:
                total += int(ch)
            k-=1
            if k:
                ns = str(total)
        return total