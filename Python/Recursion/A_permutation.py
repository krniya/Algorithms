# O(n^2*n!) | O(n*n!)
def getPermutation(array):
    permutations = []
    permutationHelper(array, [], permutations)
    return permutations

def permutationHelper(array, currentPermutation, permutations):
    if not len(array) and len(currentPermutation):
        permutations.append(currentPermutation)
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i+1:]
            newPermutation = currentPermutation + [array[i]]
            permutationHelper(newArray, newPermutation, permutations)


# O(n*n!) | O(n*n!)
def getPermutation1(array):
    permutations = []
    permutationHelper1(0, array, permutations)
    return permutations

def permutationHelper1(i, array, permutations):
    if i == len(array) - 1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(array,i,j)
            permutationHelper1(i+1, array,permutations)
            swap(array,i,j)

def swap(arr,i,j):
    arr[i], arr[j] = arr[j], arr[i]


print(getPermutation1([1,2,3,4]))