def isPal(s, i, j):
    a = s[i:j+1]
    b = s[j:i+1:-1]
    return s[i:j+1] == s[i:j-1:-1]


s = "dfsabafdg"
print(isPal(s,3,5))