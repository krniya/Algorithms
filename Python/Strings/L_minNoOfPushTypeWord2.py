def minimumPushes(word) -> int:
    count = {}
    for ch in word:
        count[ch] = count.get(ch, 0) + 1
    curr = 0
    push = 0
    for ch, cnt in count.items():
        push += cnt * ((curr // 8) + 1)
        curr += 1
    return push


def minimumPushes1(input_text: str) -> int:
    # Count letter occurrences
    letter_counts = [0] * 26
    for char in input_text:
        letter_counts[ord(char) - ord('a')] += 1
    
    # Sort counts in descending order
    sorted_counts = sorted(letter_counts, reverse=True)
    
    total_key_presses = 0
    for index, count in enumerate(sorted_counts):
        if count == 0:
            break
        total_key_presses += (index // 8 + 1) * count
    
    return total_key_presses


print(minimumPushes("abzaqsqcyrbzsrvamylmyxdjl"))