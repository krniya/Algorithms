def subArrayExists(arr):
    n_sum = 0
    s = set()
    for i in range(len(arr)):
        n_sum += arr[i]
        if n_sum == 0 or n_sum in s:
            return True
        s.add(n_sum)
    return False


print(subArrayExists([2,5,-3,-2,8]))