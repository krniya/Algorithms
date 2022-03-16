def validateStackSequences(pushed, popped):
    stack = []
    i = 0
    for x in pushed:
        stack.append(x)
        while stack and stack[-1] == popped[i]:
            i += 1
            stack.pop()
    return len(stack) == 0

print(validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))
