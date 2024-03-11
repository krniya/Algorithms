def customSortString(order: str, s: str) -> str:
    result = ""
    mp = {}
    for char in s:
        mp[char] = mp.get(char, 0) + 1
    for char in order:
        if char in mp:
            result += char * mp[char]
            del mp[char]
    for char, count in mp.items():
        result += char * count
    return result