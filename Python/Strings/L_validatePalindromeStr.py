import re
def isPalindrome(s):
    str = re.findall("[A-Za-z0-9]", s.lower())
    return str == str[::-1]
        