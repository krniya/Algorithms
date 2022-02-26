class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        mapper = {}
        maxRepeat = 0
        maxLength = 0
        for idx, letter in enumerate(s):
            if letter in mapper:
                mapper[letter] += 1
            else:
                mapper[letter] = 1
            maxRepeat = max(maxRepeat, mapper[letter])
            
            if (idx - left - maxRepeat + 1) > k:
                mapper[s[left]] -= 1
                left += 1
            maxLength = max(maxLength, idx - left + 1)
        return maxLength
