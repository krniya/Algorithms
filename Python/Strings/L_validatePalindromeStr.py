import re
def isPalindrome(s):
    str = re.findall("[A-Za-z0-9]", s.lower())
    return str == str[::-1]


def isPalindrome(s: str) -> bool:
        nStr = ""
        for ch in s:
            if ch.isalnum():
                nStr += ch.lower()
        return nStr == nStr[::-1]


def isPalindrome(s: str) -> bool:
        l,r = 0, len(s)-1
        while l<=r:
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True
        