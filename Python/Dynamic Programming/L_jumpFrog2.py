def maxJump(s) -> int:
        m = s[1]
        for i,j in zip(s[2:],s):
            m = max(m, i-j)
        return m