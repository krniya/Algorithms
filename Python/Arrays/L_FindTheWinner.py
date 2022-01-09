def findTheWinner(n, k):
    arr = [x for x in range(1, n+1)]
    i = 0
    while len(arr) != 1:
        i = i + k - 1
        while i >= len(arr):
            i -= len(arr)
        arr.pop(i)
    return arr[0]

def findTheWinner(n, k):
    res = 0
    for i in range(1, n + 1):
        res = (res + k) % i
    return res + 1

print(findTheWinner(6, 5))