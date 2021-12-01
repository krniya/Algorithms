def minJump(arr, n):
    if n<= 1:
        return 0
    if arr[0] == 0:
        return -1
    maxRange = step = arr[0]
    jump = 1
    for i in range(1,n):
        if i ==n-1:
            return jump
        maxRange =max(maxRange, i+arr[i])
        step -= 1
        if step == 0:
            jump += 1
            if(i>= maxRange):
                return -1
            step = maxRange -1
    return -1

print(minJump([1, 2, 5, 0, 1], 5))
