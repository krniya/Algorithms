def reorderedPowerOf2(N: int) -> bool:
        powers = ["".join(sorted(list( str(1<<i)))) for i in range(33)]
        target = "".join(sorted(list(str(N))))
        return target in powers