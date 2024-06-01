def scoreOfString(s: str) -> int:
    ans = 0
    for i in range(1, len(s), 1):
        ans += abs(ord(s[i - 1]) - ord(s[i]))
    return ans