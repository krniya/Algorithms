# O(n*2^n) | O(n*2^n)
def powerset(array):
    subset = [[]]
    for ele in array:
        for i in range(len(subset)):
            currentSubset = subset[i]
            subset.append(currentSubset + [ele])
    return subset

# O(n*2^n) | O(n*2^n)
def powerset1(array, index = None):
    if index is None:
        index= len(array) - 1
    elif index < 0:
        return [[]]
    ele = array[index]
    subset = powerset1(array,index-1)
    for i in range(len(subset)):
        currentSubset = subset[i]
        subset.append(currentSubset + [ele])

print(powerset1([1,2,3,4]))