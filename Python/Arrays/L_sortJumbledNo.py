def sortJumbled(mapping: list[int], nums: list[int]) -> list[int]:
    def mapn(n):
        if n==0:
            return mapping.index(0)
        mn = ""
        while n:
            mn += str(mapping[n%10])
            n = n // 10
        return int(mn[::-1] if mn else n)
    nummap = {}
    for i, n in enumerate(nums):
        nummap[n] = mapn(n)
    nums.sort(key=lambda x: nummap[x])

    return nums