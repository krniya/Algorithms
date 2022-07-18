def isValid(s: str) -> bool:
        opens = "({["
        close = ")]}"
        bMap = {"}" : "{", ")":"(", "]" : "["}
        stk = []
        for brac in s:
            if brac in opens:
                stk.append(brac)
            if brac in close:
                if not stk or stk[-1] != bMap[brac]:
                    return False
                stk.pop()
        return len(stk) == 0


def isValid(s: str) -> bool:
        Map = { ")":"(", "]":"[", "}":"{" }
        stack = []
        
        for c in s:
            if c not in Map:
                stack.append(c)
                continue    
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()
            
        return not stack