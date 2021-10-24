#O(n) | O(1)
def kadanesAlgorithm(array):
    maxEndingHere = array[0]
    maxSofar = array[0]
    for num in array[1:]:
        maxEndingHere = max(num, maxEndingHere + num)
        maxSofar = max(maxSofar, maxEndingHere)
    return maxSofar

# 1 -5 2 3 -3 2
# maxend   = 4
# maxsofar = 5


print(kadanesAlgorithm([1, 2, 4, -2, 5]))
