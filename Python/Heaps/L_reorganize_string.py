import heapq


def reorganizeString(pattern: str) -> str:
    count = {}
    for ch in pattern:
        count[ch] = count.get(ch, 0) + 1
    # n = len(pattern)
    # n = (n+1) // 2 if n%2 else n//2
    # if max([c for c in count.values()]) > n:
    #     return ""
    max_heap = [(-cnt, char) for char, cnt in count.items()]
    heapq.heapify(max_heap)
    reorg_str = ""
    prev = None
    while max_heap:
        cnt, char = heapq.heappop(max_heap)
        reorg_str += char
        if prev:
            heapq.heappush(max_heap, prev)
            prev = None
        if cnt + 1:
            prev = (cnt + 1, char)
    return reorg_str if len(reorg_str) == len(pattern) else ""
