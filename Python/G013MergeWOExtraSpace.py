def nextGap(gap):
    if (gap <= 1):
        return 0
    return (gap // 2) + (gap % 2)


def merge(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    gap = m + n
    gap = nextGap(gap)
    while gap > 0:
        i = 0
        while i + gap < n:
            if(arr1[i] > arr1[i + gap]):
                arr1[i], arr1[i+gap] = arr1[i + gap], arr1[i]
            i += 1
        j = gap - n if gap > n else 0
        while i < n and j < m:
            if (arr1[i] > arr2[j]):
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            j += 1
        if(j < m):
            j = 0
            while j + gap < m:
                if (arr2[j] > arr2[j + gap]):
                    arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]
                j += 1
        gap = nextGap(gap)


a = [2, 6, 1, 7]
b = [3, 9, 4, 8, 5]
merge(a, b)
print(a, b)


