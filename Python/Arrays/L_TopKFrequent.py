from collections import defaultdict
import heapq


def topKFrequent(nums, k):
    count = {}
    freq = [[] for i in range(len(nums)+1)]
    for num in nums:
        count[nums] = 1 + count.get(num,0)
    for n, c in count.items:
        freq[c].append(n)
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) ==k:
                return res


def topKFrequent(nums, k):
        count = {}
        hp = []
        res = []
        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n,c in count.items():
            heapq.heappush(hp,(-c,n))
        while k:
            res.append(heapq.heappop(hp)[1])
            k-=1
        return res

def topKFrequent(nums, k: int):
        counter = {}
        freq = defaultdict(list)
        res = []
        for n in nums:
            counter[n] = counter.get(n,0) + 1
        for n,c in counter.items():
            freq[c].append(n)
        for i in range(len(nums),0,-1):
            if i in freq:
                res += freq[i]
        return res[:k]