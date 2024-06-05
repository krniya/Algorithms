def count(word):
    frequency = [0] * 26
    for char in word:
        frequency[ord(char) - ord('a')] += 1
    return frequency

def intersection(freq1, freq2):
    return [min(f1, f2) for f1, f2 in zip(freq1, freq2)]

def commonChars(words):
    # Initialize the frequency array with the count of the first word
    last = count(words[0])
    
    # Update the frequency array by taking intersections with counts of remaining words
    for word in words[1:]:
        last = intersection(last, count(word))
    
    # Construct the result list
    result = []
    for i in range(26):
        result.extend([chr(i + ord('a'))] * last[i])
    
    return result 