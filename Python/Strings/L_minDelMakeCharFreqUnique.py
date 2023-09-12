def minDeletions(s: str) -> int:
    freq = [0] * 26 # Create a list to store character frequencies
    
    for c in s:
        freq[ord(c) - ord('a')] += 1 # Count the frequency of each character
    
    freq.sort() # Sort frequencies in ascending order
    
    del_count = 0 # Initialize the deletion count
    
    for i in range(24, -1, -1):
        if freq[i] == 0:
            break # No more characters with this frequency
        
        if freq[i] >= freq[i + 1]:
            prev = freq[i]
            freq[i] = max(0, freq[i + 1] - 1)
            del_count += prev - freq[i] # Update the deletion count
    
    return del_count