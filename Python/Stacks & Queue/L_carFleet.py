def carFleet(target: int, position, speed) -> int:
        pair = [[p,s] for p, s in zip(position, speed)]
        stack = []
        for position, speed in sorted(pair)[::-1]:
            stack.append((target - position) / speed)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)