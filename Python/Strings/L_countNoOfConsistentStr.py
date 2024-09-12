def countConsistentStrings(allowed: str, words) -> int:
    count = 0
    allowed = set(allowed)
    for word in words:
        for ch in word:
            if ch not in allowed:
                count+=1
                break
    return len(words) - count


print(countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))