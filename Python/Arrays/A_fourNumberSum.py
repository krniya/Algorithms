# O(n^2) | O(n^2)
def fourSum(arr, tar):
    allPairSum = {}
    quarduplet = []
    for i in range(1, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            currentSum = arr[i] + arr[j]
            difference = tar - currentSum
            if difference in allPairSum:
                for pair in allPairSum[difference]:
                    quarduplet.append(pair + [arr[i], arr[j]])
        for k in range(0, i):
            currentSum = arr[i] + arr[k]
            if currentSum not in allPairSum:
                allPairSum[currentSum] = [[arr[k], arr[i]]]
            else:
                allPairSum[currentSum].append([arr[k], arr[i]])
    return quarduplet

print(fourSum([2,4,7,8,10], 22))

