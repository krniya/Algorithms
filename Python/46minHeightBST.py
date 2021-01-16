# O(nlog(n)) | O(n)
def minHeightBST(arr):
    return constMinHeightBST(arr, None, 0, len(arr)-1)

def constMinHeightBST(arr, bst, startIdx, endIdx):
    if endIdx < startIdx:
        return
    midIdx = (startIdx + endIdx) // 2
    valueToAdd = arr[midIdx]
    if bst is None:
        bst = BST(valueToAdd)
    else:
        bst.insert(valueToAdd)
    constMinHeightBST(arr, bst, startIdx, midIdx - 1)
    constMinHeightBST(arr, bst, midIdx + 1, endIdx)
    return bst

# O(n) | O(n)
def minHeightBST1(arr):
    return constMinHeightBST1(arr, 0, len(arr)-1)

def constMinHeightBST1(arr, startIdx, endIdx):
    if endIdx < startIdx:
        return None
    midIdx = (startIdx + endIdx) // 2    
    bst = BST(arr[midIdx])
    bst.left = constMinHeightBST1(arr, startIdx, midIdx - 1)
    bst.right = constMinHeightBST1(arr, midIdx + 1, endIdx)
    return bst