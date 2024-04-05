def makeGood(s: str) -> str:
        result = []
        for c in s:
            if not result:
                result.append(c)
            elif result[-1].isupper() and result[-1].lower() == c:
                result.pop()
            elif result[-1].islower() and result[-1].upper() == c:
                result.pop()
            else:
                result.append(c)
        return ''.join(result)
    
def makeGood1(s: str) -> str:
    ss = []
    for c in s: 
        if ss and ss[-1] == c.swapcase():    # if the stack is not empty and the last letter on the stack is
            ss.pop()                         # a match for the current letter (e.g., 'a' and 'A'), remove both
        else: 
            ss.append(c)                     # continue adding to stack to compare with next letter
    
    return "".join(ss)
