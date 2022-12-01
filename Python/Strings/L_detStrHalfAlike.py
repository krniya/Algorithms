def halvesAreAlike(s: str) -> bool:
        count = 0
        vowels = set("aeiouAEIOU")
        n = len(s) // 2
        for i, ch in enumerate(s):
            if ch in vowels:
                if i < n:
                    count += 1
                else:
                    count -= 1
        return count == 0