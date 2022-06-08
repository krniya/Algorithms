def removePalindromeSub(s: str) -> int:
        if len(s) == 0:
            return 0
        if s == s[::-1]:
            return 1
        return 2

def removePalindromeSub(s: str) -> int:
        return 2 - (s==s[::-1]) - (s=="")