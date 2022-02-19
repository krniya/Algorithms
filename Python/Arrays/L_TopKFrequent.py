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