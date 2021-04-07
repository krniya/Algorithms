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

    def shiftDown(self, currIdx, endIdx, heap):
        childOneIdx = currIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currIdx * 2 + 2 if currIdx * 2 + 2 < endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxtoSwap = childTwoIdx
            else:
                idxtoSwap = childOneIdx
            if heap[idxtoSwap] < heap[currIdx]:
                self.swap(currIdx, idxtoSwap, heap)
                currIdx = idxtoSwap
                childOneIdx = currIdx * 2 + 1
            else:
                return

    def shiftUp(self, currIdx, heap):
        parentIdx = (currIdx - 1) // 2
        while currIdx > 0 and heap[currIdx] < heap[parentIdx]:
            self.swap(currIdx, parentIdx, heap)
            currIdx = parentIdx
            parentIdx = (currIdx - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap), self.heap)
        valueToRemove = self.heap.pop()
        self.shiftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove

    def insert(self, value):
        self.heap.append(value)
        self.shiftUp(len(self.heap) - 1, self.heap)

    def swap(Self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]


arr = [43, 21, 34, 64, 15, 26, 71, 18, 59]
minh = MinHeap(arr)
print(minh.heap)
