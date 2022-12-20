def canVisitAllRooms(rooms) -> bool:
        visited = set()
        toVisit = [0]
        while toVisit:
            room = toVisit.pop()
            if room in visited:
                continue
            visited.add(room)
            toVisit += rooms[room]
        return len(visited) == len(rooms)