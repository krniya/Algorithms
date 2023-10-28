def countVowelPermutation(n: int) -> int:
        if not n :
            return 0
        a = e = i = o = u = 1
        for _ in range(n - 1):
            a, e, i, o, u = e, a + i, a + e + o + u, i + u, a
        return (a + e + i + o + u) % (10**9+7)
    
    
def countVowelPermutation(n: int) -> int:
    MOD = 10**9 + 7
        
    a, e, i, o, u = 1, 1, 1, 1, 1
    
    for _ in range(1, n):
        a_next = e
        e_next = (a + i) % MOD
        i_next = (a + e + o + u) % MOD
        o_next = (i + u) % MOD
        u_next = a
        
        a, e, i, o, u = a_next, e_next, i_next, o_next, u_next
    
    return (a + e + i + o + u) % MOD