def sumOfParanthesis(s):
    stack = []
    for brack in s:
        if brack == "(":
            stack.append(-1)
        else:
            if stack[-1] == -1:
                stack.pop()
                stack.append(1)
            else:
                val = 0
                while stack[-1] != -1:
                    val += stack.pop()
                stack.pop()
                stack.append(2*val)
    return stack[0] if len(stack) == 1 else sum(stack)

print(sumOfParanthesis("()()(())"))