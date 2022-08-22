from cmath import log


def isPowerOfFour(num: int) -> bool:
        return num>0 and log(num,4).is_integer()