
def maximumValue(strs) -> int:
        res = 0
        for word in strs:
            if word.isnumeric():
                res = max(res, int(word))
            else:
                res = max(res, len(word))
        return res

