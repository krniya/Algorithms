def checkDistances( s: str, distance) -> bool:
        distMap = {}
        for i,ch in enumerate(s):
            if ch not in distMap:
                distMap[ch] = i
            else:
                distMap[ch] = i - distMap[ch] - 1
        for ch, val in distMap.items():
            if distance[ord(ch) - ord('a')] != val:
                return False
        return True