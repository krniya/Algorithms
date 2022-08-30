def largestRectangleArea(heights):
        stack = []
        maxRec = 0
        for idx, height in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > height:
                prevIdx, prevHeight = stack.pop()
                maxRec = max(maxRec, prevHeight * (idx - prevIdx))
                start = prevIdx
            stack.append([start, height])
        for idx, height in stack:
            maxRec = max(maxRec, height * (len(heights) - idx))
        return maxRec