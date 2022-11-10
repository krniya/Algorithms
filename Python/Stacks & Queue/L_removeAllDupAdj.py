def removeDuplicates(s: str) -> str:
    stack = []
    for ch in s:
        if not stack or stack[-1] != ch:
            stack.append(ch)
        else:
            stack.pop()
    return "".join(stack)