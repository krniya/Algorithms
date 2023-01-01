def wordPattern(pattern: str, s: str) -> bool:
        hashmap = {}
        s = s.split(" ")
        
        if len(pattern) != len(s):
            return False
        if len(set(pattern)) != len(set(s)):
            return False

        for i, ch in enumerate(pattern):
            if ch not in hashmap:
                hashmap[ch] = s[i]
            else:
                if hashmap[ch] != s[i]:
                    return False
        return True