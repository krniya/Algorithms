def sort012(arr):
    min = mid = 0
    max = len(arr) - 1
    while mid < max:
        if arr[mid] == 0:
            arr[min], arr[mid] = arr[mid], arr[min]
            mid += 1
            min += 1
        elif arr[mid] == 2:
            arr[mid], arr[max] = arr[max], arr[mid]
            max -= 1
        else:
            mid += 1
    return arr


print(sort012([0, 2, 1, 1, 2, 0, 1, 0, 0, 2, 2, 1, 0, 2]))
