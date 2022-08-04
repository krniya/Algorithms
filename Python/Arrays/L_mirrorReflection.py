def mirrorReflection(self, p: int, q: int) -> int:
        k = 1
        while (q * k % p): k += 1
        if q * k / p % 2 and k % 2: return 1
        if q * k / p % 2 == 0 and k % 2: return 0
        if q * k / p % 2 and k % 2 == 0: return 2
        return -1