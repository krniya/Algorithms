from collections import defaultdict


def numMatchingSubseq(S: str, words) -> int:
        word_dict = defaultdict(list)
        count = 0
        for word in words:
            word_dict[word[0]].append(word)                  
        for char in S:
            words_expecting_char = word_dict[char]
            word_dict[char] = []
            for word in words_expecting_char:
                if len(word) == 1:
                    count += 1
                else:
                    word_dict[word[1]].append(word[1:])
        return count

print(numMatchingSubseq("abcde", ["a","bb","acd","ace"]))