def longestValidParensthesis(s: str) -> int:
    stk, max_len = [(")", -1)], 0
    for i in range(len(s)):
        if s[i] == ")" and stk[-1][0] == "(":
            stk.pop()
            max_len = max(max_len, i-stk[-1][1])
        else:
            stk.append((s[i], i))
    return max_len


print(longestValidParensthesis(')(()())(())))()'))
