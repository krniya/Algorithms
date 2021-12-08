def countPairs(arr, k):
    pairs = {}
    for num in arr:
        if num in pairs:
            pairs[num] += 1
        else:
            pairs[num] =1
    twice_count = 0
    for num in arr:
        if (k-num) in pairs:
            twice_count += pairs[k - num]
        if (k - num == num):
            twice_count -= 1
    return int(twice_count / 2)

print(countPairs([3,2,4,3,1], 5))