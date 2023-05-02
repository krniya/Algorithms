def arraySign(nums) -> int:
    signFunc = 1
    for number in nums:
        if number == 0:
            return 0
        if number < 0:
            signFunc *= -1
    return signFunc
