# O(n^2) | O(1)
def longestpalindromeSubstring(str):
    currentLongest = [0, 1]
    for i in range(1, len(str)):
        odd = getLongestPalindrome(str, i-1, i+1)
        even = getLongestPalindrome(str, i-1, i)
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        currentLongest = max(longest, currentLongest,
                             key=lambda x: x[1] - x[0])
    return str[currentLongest[0]:currentLongest[1]]


def getLongestPalindrome(str, left, right):
    while left >= 0 and right < len(str):
        if str[left] != str[right]:
            break
        left -= 1
        right += 1
    return [left + 1, right]


print(longestpalindromeSubstring('asdfaffgdsdfsfsfsdfsd'))
