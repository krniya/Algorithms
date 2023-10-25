def kthGrammar(n: int, k: int) -> int:
    if n == 1:
        return 0
    length = 2 ** (n - 2)
    if k <= length:
        return kthGrammar(n - 1, k)
    else:
        return 1 - kthGrammar(n - 1, k - length)