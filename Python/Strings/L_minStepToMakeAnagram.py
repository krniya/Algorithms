def minSteps(s: str, t: str) -> int:
    count_s = [0] * 26
    count_t = [0] * 26

    for char in s:
        count_s[ord(char) - ord('a')] += 1

    for char in t:
        count_t[ord(char) - ord('a')] += 1

    steps = 0
    for i in range(26):
        steps += abs(count_s[i] - count_t[i])

    return steps // 2