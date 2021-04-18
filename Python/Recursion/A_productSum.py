# Time O(n) | Space O(d)
def productSum(arr, multiplier = 1):
    sum = 0
    for i in arr:
        if type(i) is list:
            sum += productSum(i, multiplier + 1)
        else:
            sum += i
    return sum * multiplier

print(productSum([2,[1,2],3]))
