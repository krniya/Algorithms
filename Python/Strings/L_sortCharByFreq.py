from collections import Counter


def frequencySort(s: str) -> str:
        counter = {}
        for ch in s:
            counter[ch] = 1 + counter.get(ch, 0)
        res = ""
        for k in sorted(counter, key=counter.get, reverse=True):
            res += k * counter[k]
        return res
    
    
def frequencySort(s: str) -> str:
        counter = Counter(s)
        pq = [(-freq, char) for char, freq in counter.items()]
        heapq.heapify(pq)
        result = ''
        while pq:
            freq, char = heapq.heappop(pq)
            result += char * -freq
        return result