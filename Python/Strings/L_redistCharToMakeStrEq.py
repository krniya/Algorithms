from collections import defaultdict
from typing import List


def makeEqual(words: List[str]) -> bool:
    char_count = defaultdict(int)
    for word in words:
        for char in word:
            char_count[char] += 1
    word_length = len(words)
    for count in char_count.values():
        if count % word_length != 0:
            return False
    return True