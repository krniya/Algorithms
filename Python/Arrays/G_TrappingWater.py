def trappingWater(height):
    n = len(height)
    maxLeft, maxRight = [0] * n, [0] * n    
    for i in range(1, n):
        maxLeft[i] = max(height[i-1], maxLeft[i-1])
    for i in range(n-2, -1, -1):
        maxRight[i] = max(height[i+1], maxRight[i+1])    
    ans = 0
    for i in range(n):
        waterLevel = min(maxLeft[i], maxRight[i])
        if waterLevel >= height[i]:
            ans += waterLevel - height[i]
    return ans

def trappingWater2(height):
    l,r = 0, len(height) - 1
    res = ml = mr = 0
    while l <= r:
        if height[l] <= height[r]:
            if height[l] >= ml:
                ml = height[l]
            else:
                res += ml - height[l]
            l+=1
        else:
            if height[r] >= mr:
                mr = height[r]
            else:
                res += mr - height[r]
            r-=1
    return res

print(trappingWater2([3,0,0,2,0,4]))