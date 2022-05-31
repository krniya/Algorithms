def hasAllCodes(s: str, k: int) -> bool:
        countSet = set()
        for i in range(len(s)-k+1):
            countSet.add(s[i:i+k])
        return len(countSet) == 2 ** k