def rangeBitwiseAnd(left: int, right: int) -> int:
    cnt = 0
    while left != right:
        left >>= 1
        right >>= 1
        cnt += 1
    return left << cnt
