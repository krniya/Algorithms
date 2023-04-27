def bulbSwitch(n: int) -> int:
    i = 0
    while True:
        if i * i > n:
            return i-1
        i += 1
