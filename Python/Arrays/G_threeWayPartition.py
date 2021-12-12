def threeWayPartition(arr, a, b):
    min = mid = 0
    max = len(arr) - 1
    while mid < max:
        if arr[mid] < a:
            arr[min], arr[mid] = arr[mid], arr[min]
            mid += 1
            min += 1
        elif arr[mid] > b:
            arr[mid], arr[max] = arr[max], arr[mid]
            max -= 1
        else:
            mid += 1
    return arr

def threeWayPartition2(array, a, b):
    n = len(array)
    s = i = 0
    e = n-1	
    while(i <= e):
        if array[i] < a:
            array[i],array[s] = array[s],array[i]
            i+=1
            s+=1
        elif array[i] > b:
            array[i],array[e] = array[e],array[i]
            e-=1
        else:
            i+=1
    return array

print(threeWayPartition([76, 8, 75, 22, 59, 96, 30, 38, 36], 44,62))