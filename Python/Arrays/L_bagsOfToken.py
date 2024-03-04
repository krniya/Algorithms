from typing import List


def bagOfTokensScore(tokens: List[int], power: int) -> int:
    tokens.sort()
    max_score = curr_score = 0
    left, right = 0, len(tokens) - 1
    while left <= right:
        if power >= tokens[left]:
            power -= tokens[left]
            left += 1
            curr_score += 1
            max_score = max(max_score, curr_score)
        elif curr_score > 0:
            power += tokens[right]
            right -= 1
            curr_score -=1
        else:
            break
    return max_score