def firstUniqChar(s: str) -> int:
    counter = {}
    for ch in s:
        counter[ch] = counter.get(ch, 0) + 1
    
    for idx, char in enumerate(s):
        if counter[char] == 1:
            return idx
    
    return - 1