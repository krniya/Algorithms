# O(n) | O(n)
def balancedBracket(str):
    openningBracket = "[{("
    closeingBracket = ")}]"
    matchingBracket = {")": "(", "]": "[", "}": "{"}
    stack = []
    for char in str:
        if char in openningBracket:
            stack.append(char)
        elif char in closeingBracket:
            if len(stack) == 0:
                return False
            if stack[-1] == matchingBracket[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0