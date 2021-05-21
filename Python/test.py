def twoSum(num, target):
    map = {}
    for i in range(len(num)):
        if num[i] not in map:
            map[target - num[i]] = i
        else:
            return map[num[i]], i + 1
    return -1, -1


print(twoSum([2, 5, 7, 1, 3, 9], 11))
