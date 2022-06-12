import collections


def matchReplacement(s: str, sub: str, mappings) -> bool:
        h = collections.defaultdict(set)
        for a,b in mappings:
            h[a].add(b)
        l = len(sub)
        for i in range(len(s)-len(sub)+1):
            flag =True
            for s_val, sub_val in zip(s[i:i+l], sub):
                if s_val==sub_val or (s_val in h[sub_val]): continue
                else:
                    flag = False
                    break
            if flag: 
                return True
        return False

print(matchReplacement("fool3e7bar","leet",[["e","3"],["t","7"],["t","8"]]))