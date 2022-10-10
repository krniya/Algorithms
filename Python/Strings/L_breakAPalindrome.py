def breakPalindrome(palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        for i in range(n//2):
            if palindrome[i] != 'a':
                t = palindrome[:i] + "a" + palindrome[i+1:]
                if t != t[::-1]:
                    return t
        return palindrome[:n-1] + "b"