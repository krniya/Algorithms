def sortVowels(s: str) -> str:
    vowels = "AEIOUaeiou"
    owned_vowels = []
    for ch in s:
        if ch in vowels:
            owned_vowels.append(ch)
    owned_vowels.sort()
    sort_vowel_s = ""
    i = 0
    for ch in s:
        if ch not in vowels:
            sort_vowel_s += ch
        else:
            sort_vowel_s += owned_vowels[j]
            i += 1
    return sort_vowel_s


