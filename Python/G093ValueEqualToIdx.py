def valEqToIdx(arr):
    ans = []
    i, j = 0, len(arr)-1
    while i <= j:
        if arr[i] == i+1:
            ans.append(i+1)
        if arr[j] == j+1:
            ans.append(j+1)
        i += 1
        j -= 1
    ans = list(set(ans))
    return ans


print(valEqToIdx([356, 768, 656, 575, 32, 53, 351, 8, 942, 725, 967, 431, 108, 192, 8, 338, 458,
                  288, 754, 384, 946, 910, 210, 759, 222, 589, 423, 947, 507, 31, 414, 169, 901, 592, 763, 656, 41]))
