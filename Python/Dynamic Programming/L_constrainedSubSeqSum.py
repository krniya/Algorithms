import collections
from typing import List


def constrainedSubsetSum(A: List[int], k: int) -> int:
    deque = collections.deque()
    for i in range(len(A)):
        A[i] += deque[0] if deque else 0
        while len(deque) and A[i] > deque[-1]:
            deque.pop()
        if A[i] > 0:
            deque.append(A[i])
        if i >= k and deque and deque[0] == A[i - k]:
            deque.popleft()
    return max(A)