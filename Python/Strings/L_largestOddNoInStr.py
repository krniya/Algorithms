def largestOddNumber(num: str) -> str:
    str_len = len(num)
    for i in range(str_len-1, -1, -1):
        if int(num[i]) % 2 != 0:
            return num[:i+1]
    return ""