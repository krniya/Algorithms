# Brute Force
# Time O(n^m * m)
# Space O(m)

# def howSum(tar, arr):
#     if tar == 0:
#         return []
#     if tar < 0:
#         return None
#     for num in arr:
#         rem = tar - num
#         remRes = howSum(rem, arr)
#         if remRes is not None:
#             return remRes + [num]
#     return None


def howSum(tar, arr, memo={}):
    if tar in memo:
        return memo[tar]
    if tar == 0:
        return []
    if tar < 0:
        return None
    for num in arr:
        rem = tar - num
        remRes = howSum(rem, arr, memo)
        if remRes is not None:
            memo[tar] = remRes + [num]
            return memo[tar]
    memo[tar] = None
    return None


print(howSum(300, [7, 8]))
