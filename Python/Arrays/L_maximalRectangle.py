from typing import List


def maximalRectangle(matrix: List[List[str]]) -> int:
    if not matrix:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    heights = [0] * (cols + 1)  # Include an extra element for easier calculation
    max_area = 0
    for row in matrix:
        for i in range(cols):
            heights[i] = heights[i] + 1 if row[i] == '1' else 0
        # Calculate max area using histogram method
        stack = []
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
    return max_area               