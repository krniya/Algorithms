def maxLengthBetweenEqualCharacters(s: str) -> int:
    visited = {}
    max_length = -1
    for i, char in enumerate(s):
        if char in visited:
            max_length = max(max_length, i-visited[char]-1)
        else:
            visited[char] = i
    return max_length
