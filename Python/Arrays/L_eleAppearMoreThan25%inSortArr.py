def findSpecialInteger(arr) -> int:
    size = len(arr)
    quater = size // 4
    count = 1
    curr = arr[0]
    for i in range(1, size):
        if curr == arr[i]:
            count += 1
        else:
            count = 1
        if count > quater:
            return arr[i]
        curr = arr[i]
    return curr