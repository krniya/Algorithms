def maxArea(height):
    l, r = 0, len(height) - 1
    maxWater = 0
    while l < r:
        currMax = min(height[l], height[r]) * (r-l)
        maxWater = max(currMax, maxWater)
        if height[l] < height[r]:
            l+=1
        else:
            r-=1
    return maxWater

print(maxArea(
[2,3,4,5,18,17,6]))