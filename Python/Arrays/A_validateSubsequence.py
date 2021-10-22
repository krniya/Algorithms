# O(n) | O(1)
def validateSubsequence(arr, ssq):
    arrSeq = 0
    subSeq = 0
    while arrSeq < len(arr) and subSeq < len(ssq):
        if arr[arrSeq] == ssq[subSeq]:
            subSeq += 1
        arrSeq += 1
    return subSeq == len(ssq)


print(validateSubsequence([2, 5, 3, 8, 6, 7, 4, 1], [5, 7, 1]))
