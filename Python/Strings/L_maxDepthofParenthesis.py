def maxDepth(s: str) -> int:
    max_dept = 0
    curr_dept = 0
    for ch in s:
        if ch == "(":
            curr_dept += 1
        if ch == ")":
            curr_dept -= 1
        max_dept = max(max_dept, curr_dept)
    return max_dept