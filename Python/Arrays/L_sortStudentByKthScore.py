from typing import List

def sortTheStudents(A: List[List[int]], k: int) -> List[List[int]]:
        return sorted(A, key=lambda a: -a[k])