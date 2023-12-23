def isPathCrossing(path: str) -> bool:
    visited = set()
    visited.add(tuple([0,0]))
    directions = {
        'N' : [0, 1],
        'S' : [0,-1],
        'E' : [1, 0],
        'W' : [-1,0]
    }
    current_position = [0,0]
    for direction in path:
        current_position[0] += directions[direction][0]
        current_position[1] += directions[direction][1]
        if tuple(current_position) in visited:
            return True
        visited.add(tuple(current_position))
    return False

print(isPathCrossing("NESWW"))