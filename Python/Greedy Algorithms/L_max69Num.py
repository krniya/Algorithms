def maximum69Number (num: int) -> int:
        num = str(num)
        for i,ch in enumerate(num):
            if ch == "6":
                return int(num[:i] + "9" + num[i+1:])
        return num