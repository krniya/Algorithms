# Time: O(n^m * m) Space: O(m^2)

def bestSum(targetSum, numbers):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    soretest = None
    for num in numbers:
        rem = targetSum - num
        remComb = bestSum(rem, numbers)
        if remComb != None:
            comb = remComb + [num]
            if soretest == None or len(comb) < len(soretest):
                soretest = comb
    return soretest

# Time: O() Space: O()


def bestSum2(targetSum, numbers, memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    soretest = None
    for num in numbers:
        rem = targetSum - num
        remComb = bestSum(rem, numbers, memo)
        if remComb != None:
            comb = remComb + [num]
            if soretest == None or len(comb) < len(soretest):
                soretest = comb

    memo[targetSum] = soretest
    return soretest


print(bestSum(7, [2, 3, 4, 7]))
