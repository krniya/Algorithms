class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_chars = {}
        set_vals = set()
        for i in range(len(s)):
            if s[i] in map_chars:
                if map_chars[s[i]] != t[i]:
                    return False
            else:
                if t[i] in set_vals:
                    return False
                map_chars[s[i]] = t[i]
                set_vals.add(t[i])
        return True
