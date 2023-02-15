from typing import List

def addToArrayForm(A: List[int], K: int) -> List[int]:
        for i in range(len(A) - 1, -1, -1):
            K, A[i] = divmod(A[i] + K, 10)
        return [int(i) for i in str(K)] + A if K else A