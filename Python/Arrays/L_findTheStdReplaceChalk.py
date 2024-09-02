def chalkReplacer(chalk, k: int) -> int:
    total = sum(chalk)
    rem = k % total
    for i, value in enumerate(chalk):
        rem -= value
        if rem < 0:
            return i
    return -1 