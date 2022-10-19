from collections import defaultdict
import heapq

class Node:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
    
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq
    

def topKFrequent(words, k: int):
    mapper = defaultdict(int)
    for word in words:
        mapper[word] += 1
    
    h = list()
    for word, freq in mapper.items():
        node = Node(word, freq)
        if len(h) == k:
            heapq.heappushpop(h, node)
        else:
            heapq.heappush(h, node)
            
    result = list()
    while h:
        result.append(heapq.heappop(h).word)
    return result[::-1]

print(topKFrequent(["i","love","leetcode","i","love","coding"], 2))