class MinHeap:
    def __init__(self, arr) -> None:
        self.heap = self.buildHeap(arr)

    def heap(self):
        return self.heap

    def buildHeap(self, arr):
        firstParentIdx = (len(arr) - 2) // 2
        for currIdx in reversed(range(firstParentIdx + 1)):
            self.shiftDown(currIdx, len(arr) - 1, arr)
        return arr

    def shiftDown(Self, currIdx, endIdx, heap):
        childOneIdx = currIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currIdx * 2 + 2 if currIdx * 2 + 2 < endIdx else -1
