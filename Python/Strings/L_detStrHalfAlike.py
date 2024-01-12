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
    
def halvesAreAlike1(s: str) -> bool:
    def vowel_count(half: str) -> int:
        vowels = "aeiouAEIOU"
        count = 0
        for ch in half:
            if ch in vowels:
                count +=1
        return count
    mid_point = len(s) // 2
    return vowel_count(s[:mid_point]) == vowel_count(s[mid_point:])

print((halvesAreAlike1("book")))