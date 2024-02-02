from typing import List


def sequentialDigits(low: int, high: int) -> List[int]:
    sequences = []
    for i in range(1,10):
        num = i
        next_digit = i + 1
        while num <= high and next_digit <= 9:
            num = num * 10 + next_digit
            if low <= num <= high:
                sequences.append(num)
            next_digit += 1
    sequences.sort()
    return sequences
            