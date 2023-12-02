def countCharacters(words, chars):
    char_count = [0] * 26
    # Step 1: Initialize Character char_count Array
    for ch in chars:
        char_count[ord(ch) - ord('a')] += 1
    def can_Form(word):
        local_count = [0] * 26
        # Step 2: Update char_count Array
        for ch in word:
            x = ord(ch) - ord('a')
            local_count[x] += 1
            if local_count[x] > char_count[x]:
                return False
        return True
    total_good_string = 0
    # Step 3: Check Words
    for word in words:
        if can_Form(word):
            # Step 4: Calculate Lengths
            total_good_string += len(word)
    return total_good_string

    