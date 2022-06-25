def countAsterisks(s: str) -> int:
        s = s.split("|")
        c = 0
        for a in s[0::2]:
            c += a.count("*")
        return c