def isReachableAtTime(sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
    if  (sx, sy) == (fx, fy):
        return t != 1
    dx = abs(fx - sx)
    dy = abs(fy - sy)
    return t >= max(dx, dy)