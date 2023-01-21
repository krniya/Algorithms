from typing import List

def restoreIpAddresses(s: str) -> List[str]:
        def backtrack(s, ct, path, rst):
            if ct == 4:
                #have 4 chunk and use up all digits
                if not s: rst.append(path[:-1]) 
                return
            for i in range(1, 4):
                #prevent index overflow
                if i > len(s): continue
                #take 1 digit is always good
                #take 2 or 3 digits, first digit cannot be '0'
                if i > 1 and s[0] == '0': continue
                #take 3 digits, cannot greater than 255
                if i > 2 and int(s[:3]) > 255: continue
                backtrack(s[i:], ct+1, path + s[:i] + '.', rst)
            
        rst = []
        backtrack(s, 0, '', rst)
        return rst