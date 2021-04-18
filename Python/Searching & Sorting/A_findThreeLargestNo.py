# time: O(n)| Space: O(1)
def findThreeLargestNo(arr):
    threeLargest = [None, None, None]
    for num in arr:
        updateLargest(threeLargest, num)
    return threeLargest


def updateLargest(threeLargest, num):
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate(threeLargest, num, 2)
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num, 1)
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate(threeLargest, num, 0)


def shiftAndUpdate(arr, num, idx):
    for i in range(idx + 1):
        if idx == i:
            arr[i] = num
        else:
            arr[i] = arr[i+1]


array = [12,-6,54,654,43,75,234,45,6,98,76]
print(findThreeLargestNo(array))