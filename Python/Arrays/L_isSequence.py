class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        remainder_of_t = iter(t)
        for letter in s:
            if letter not in remainder_of_t:
                  return False
        return True
