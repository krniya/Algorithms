def first(arr, low, high):
    if high >= low:
        mid = low + (high - low)//2
        if (mid == 0 or arr[mid - 1] == 0) and arr[mid] == 1:
            return mid
        elif arr[mid] == 0:
            return first(arr, (mid + 1), high)
        else:
            return first(arr, low, (mid - 1))
    return -1


def rowWithMax1s(mat):
    R = len(mat)
    C = len(mat[0])
    max_row_index = 0
    max = -1
    for i in range(0, R):
        index = first(mat[i], 0, C - 1)
        if index != -1 and C - index > max:
            max = C - index
            max_row_index = i
    return max_row_index


# Driver Code
mat = [[0, 0, 0, 1],
       [0, 1, 1, 1],
       [1, 1, 1, 1],
       [0, 0, 0, 0]]

print(rowWithMax1s(mat))
