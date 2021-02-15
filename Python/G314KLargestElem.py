# O(n * k) | O(k)

from collections import deque
import heapq


def max_of_all_in_k(arr, n):
    i = 0
    j = k-1
    heap = arr[i:j + 1]
    heapq._heapify_max(heap)
    print(heap[0], end=" ")
    last = arr[i]
    i += 1
    j += 1
    nexts = arr[j]
    while j < n:
        heap[heap.index(last)] = nexts
        heapq._heapify_max(heap)
        print(heap[0], end=" ")
        last = arr[i]
        i += 1
        j += 1
        if j < n:
            nexts = arr[j]

# O(n) | O(k)


def printMax(arr, n, k):
    Qi = deque()
    for i in range(k):
        while Qi and arr[i] >= arr[Qi[-1]]:
            Qi.pop()
        Qi.append(i)
    for i in range(k, n):
        print(str(arr[Qi[0]]) + " ", end="")
        while Qi and Qi[0] <= i-k:
            Qi.popleft()
        while Qi and arr[i] >= arr[Qi[-1]]:
            Qi.pop()
        Qi.append(i)
    print(str(arr[Qi[0]]))


if __name__ == "__main__":
    arr = [12, 1, 78, 90, 57, 89, 56]
    k = 3
    printMax(arr, len(arr), k)
