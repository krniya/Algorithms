def gcdOfStrings(str1: str, str2: str) -> str:
        if not str1 or not str2:
            return str1 if str1 else str2
        elif len(str1) < len(str2):
            return gcdOfStrings(str2, str1)
        elif str1[: len(str2)] == str2:
            return gcdOfStrings(str1[len(str2) :], str2)
        else:
            return ''