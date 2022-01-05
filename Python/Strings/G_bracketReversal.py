import math

def countMinReversals(expr):
    length = len(expr)
    if (length % 2 != 0):
        return -1
    left_brace = 0
    right_brace = 0
    for i in range(length):
        if (expr[i] == '{'):
            left_brace += 1
        else:
            if (left_brace == 0):
                right_brace += 1
            else:
                left_brace -= 1
    ans = math.ceil(left_brace / 2) + math.ceil(right_brace / 2)
    return ans

print(countMinReversals("}{{}}{{{"))