def greatestLetter(s: str) -> str:
        seen = set()
        for char in s:
            seen.add(char)
        for i in range(ord("Z"), ord("A")-1, -1):
            if chr(i) in seen and chr(i-(ord("A")-ord("a"))) in seen:
                return chr(i)
        return ""