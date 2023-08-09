from typing import List


def minimize_max(numbers: List[int], no_of_pairs: int) -> int:
    """Minimize maximum differnce of pairs in array

    Args:
        numbers (List[int]): _description_
        no_of_pairs (int): _description_

    Returns:
        int: _description_
    """
    def is_valid(threshold):
        i, count = 0, 0
        while i < len(numbers) - 1:
            if abs(numbers[i] - numbers[i+1]) <= threshold:
                count += 1
                i += 2
            else:
                i += 1
            if count == no_of_pairs:
                return True
        return False
    if no_of_pairs == 0:
        return 0
    numbers.sort()
    left, right = 0, numbers[-1]
    result = 10 ** 9
    while left <= right:
        mid_point = left + (right - left) // 2
        if is_valid(mid_point):
            result = mid_point
            right = mid_point - 1
        else:
            left = mid_point + 1
    return result
