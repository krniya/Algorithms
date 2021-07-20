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


print(bestSum(7, [2, 3, 4, 7]))
