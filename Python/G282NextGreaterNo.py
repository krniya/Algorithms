def nextLargerElement(arr):
    ans = []
    i = 0
    j = 0
    while i < len(arr):
        j = i
        while j < len(arr):
            if arr[i] < arr[j]:
                ans.append(arr[j])
                break
            j += 1
        if j == len(arr):
            ans.append(-1)
        i += 1
    return ans


print(nextLargerElement([1, 3, 2, 4]))
