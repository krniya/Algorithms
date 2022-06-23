import heapq


def scheduleCourse(courses) -> int:
        s = []
        start = 0
        for t, end in sorted(courses, key=lambda c: c[1]):
            start += t
            heapq.heappush(s, -t)
            if start > end:
                nt = heapq.heappop(s)
                start += nt
        return len(s)