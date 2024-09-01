def isValid(s):
        #your code goes here
        opening = "({["
        mapping = { "]":"[", "}":"{", ")":"(" }
        stack = []
        for par in s:
            if par in opening:
                stack.append(par)
            else:
                if not stack or stack[-1] != mapping[par]:
                    return False
                stack.pop()
        return len(stack) == 0
    
    
print(isValid("{{[]()}}"))