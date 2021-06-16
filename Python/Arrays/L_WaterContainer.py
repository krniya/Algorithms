def waterContainer(height):
    i, j = 0, len(height) - 1
    water = 0
    while i < j:
        water = max(water, min(height[i], height[j]) * (j - i))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return water
